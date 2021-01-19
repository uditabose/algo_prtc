import math
from dynamic import Dynamic


class MinimumCoinChange(Dynamic):
    def __init__(self, denomination, total):
        self.denomination = denomination
        self.total = total

    def bruteforce(self):
        return MinimumCoinChange.__recurse__(self.denomination, self.total, 0)

    @staticmethod
    def __recurse__(denomination, total, current):
        if total == 0:
            return 0

        dn = len(denomination)
        if current >= dn:
            return math.inf

        change_with_current = math.inf
        if total >= denomination[current]:
            change_with_current = MinimumCoinChange.__recurse__(denomination, total - denomination[current], current)
            if change_with_current != math.inf:
                change_with_current += 1

        change_without_current = MinimumCoinChange.__recurse__(denomination, total, current + 1)

        return min(change_with_current, change_without_current)

    def topdown(self):
        memo = [[-1 for _ in range(self.total + 1)] for _ in range(len(self.denomination))]
        return MinimumCoinChange.__recurse_memo__(self.denomination, self.total, 0, memo)

    @staticmethod
    def __recurse_memo__(denomination, total, current, memo):
        if total == 0:
            return 0

        dn = len(denomination)
        if current >= dn:
            return math.inf

        if memo[current][total] != -1:
            return memo[current][total]

        change_with_current = math.inf
        if total >= denomination[current]:
            change_with_current = MinimumCoinChange.__recurse_memo__(denomination, total - denomination[current], current, memo)
            if change_with_current != math.inf:
                change_with_current += 1

        change_without_current = MinimumCoinChange.__recurse_memo__(denomination, total, current + 1, memo)

        memo[current][total] = min(change_with_current, change_without_current)
        # print(memo)
        return memo[current][total]

    def bottomup(self):
        pass
        dn = len(self.denomination)
        table = [[math.inf for _ in range(self.total + 1)] for _ in range(dn)]
        for i in range(dn):
            table[i][0] = 0

        for denom in range(dn):
            for tot in range(1, self.total + 1):
                change_with_current = math.inf
                change_without_current = math.inf
                if denom > 0:
                    change_with_current = table[denom - 1][tot]
                    if change_with_current != math.inf:
                        change_with_current += 1

                if self.denomination[denom] <= tot:
                    change_without_current = table[denom][tot - self.denomination[denom]]

                table[denom][tot] = min(change_with_current, change_without_current)

        print(table)
        return table[-1][self.total]


if __name__ == '__main__':
    d = [1, 2, 3]
    t = 5
    MinimumCoinChange(d, t).all_result()
