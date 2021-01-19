from dynamic import Dynamic
import math


class MaximumRibbonCut(Dynamic):
    def __init__(self, pieces, length):
        self.pieces = pieces
        self.length = length

    def bruteforce(self):
        return MaximumRibbonCut.__recurse__(self.pieces, self.length, 0)

    @staticmethod
    def __recurse__(pieces, length, current):
        if length <= 0:
            return 0
        if current >= len(pieces):
            return -math.inf

        pieces_with_current = -math.inf
        if pieces[current] <= length:
            pieces_with_current = MaximumRibbonCut.__recurse__(pieces, length - pieces[current], current)
            if pieces_with_current != -math.inf:
                pieces_with_current += 1

        pieces_without_current = MaximumRibbonCut.__recurse__(pieces, length, current + 1)

        return max(pieces_without_current, pieces_with_current)

    def topdown(self):
        memo = [[-math.inf for _ in range(self.length + 1)] for _ in range(len(self.pieces))]
        return MaximumRibbonCut.__recurse_memo__(self.pieces, self.length, 0, memo)

    @staticmethod
    def __recurse_memo__(pieces, length, current, memo):
        if length <= 0:
            return 0
        if current >= len(pieces):
            return -math.inf

        if memo[current][length] != -math.inf:
            return memo[current][length]

        pieces_with_current = -math.inf
        if pieces[current] <= length:
            pieces_with_current = MaximumRibbonCut.__recurse_memo__(pieces, length - pieces[current], current, memo)
            if pieces_with_current != -math.inf:
                pieces_with_current += 1

        pieces_without_current = MaximumRibbonCut.__recurse_memo__(pieces, length, current + 1, memo)

        memo[current][length] = max(pieces_without_current, pieces_with_current)
        # print(memo)
        return memo[current][length]

    def bottomup(self):
        pn = len(self.pieces)
        table = [[-math.inf for _ in range(self.length + 1)] for _ in range(pn)]

        for i in range(pn):
            table[i][0] = 0

        for np in range(pn):
            for nl in range(1, self.length + 1):
                pieces_with_current = -math.inf
                if self.pieces[np] <= nl:
                    pieces_with_current = table[np][nl - self.pieces[np]]
                    if pieces_with_current != -math.inf:
                        pieces_with_current += 1

                pieces_without_current = -math.inf
                if np > 0:
                    pieces_without_current = table[np - 1][nl]

                table[np][nl] = max(pieces_with_current, pieces_without_current)

        print(table)
        return table[-1][-1]


if __name__ == '__main__':
    p = [2, 3, 5]
    l = 5
    MaximumRibbonCut(p, l).all_result()
