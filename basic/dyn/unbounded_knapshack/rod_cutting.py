from typing import *
from dynamic import Dynamic


class RodCutting(Dynamic):
    def __init__(self, lengths, prices, rod_length):
        self.lengths = lengths
        self.prices = prices
        self.rod_length = rod_length

    def bruteforce(self):
        return RodCutting.__recurse__(self.lengths, self.prices, self.rod_length, 0)

    @staticmethod
    def __recurse__(lengths, prices, rod_length, current):
        if current >= len(lengths):
            return 0

        profit_with_current = 0
        if lengths[current] <= rod_length:
            profit_with_current = prices[current] + \
                                    RodCutting.__recurse__(lengths, prices, rod_length - lengths[current], current)

        profit_without_current = RodCutting.__recurse__(lengths, prices, rod_length, current + 1)

        return max(profit_with_current, profit_without_current)

    def topdown(self):
        memo = [[-1 for _ in range(self.rod_length + 1)] for _ in range(len(self.lengths))]
        return RodCutting.__recurse_memo__(self.lengths, self.prices, self.rod_length, 0, memo)

    @staticmethod
    def __recurse_memo__(lengths, prices, rod_length, current, memo):
        if current >= len(lengths):
            return 0

        if memo[current][rod_length] != -1:
            return memo[current][rod_length]

        profit_with_current = 0
        if lengths[current] <= rod_length:
            profit_with_current = prices[current] + \
                                  RodCutting.__recurse_memo__(lengths, prices, rod_length - lengths[current], current, memo)

        profit_without_current = RodCutting.__recurse_memo__(lengths, prices, rod_length, current + 1, memo)

        memo[current][rod_length] = max(profit_with_current, profit_without_current)
        # print(memo)
        return memo[current][rod_length]

    def bottomup(self):
        ln = len(self.lengths)
        rn = self.rod_length + 1
        table = [[0 for _ in range(rn)] for _ in range(ln)]

        for i in range(ln):
            for j in range(1, rn):
                profit_with_current = 0
                if self.lengths[i] <= j:
                    profit_with_current = self.prices[i] + table[i][j - self.lengths[i]]

                profit_without_current = 0
                if i > 0:
                    profit_without_current = table[i - 1][j]

                table[i][j] = max(profit_with_current, profit_without_current)

        # print(table)
        return table[-1][self.rod_length]


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5]
    p = [2, 6, 7, 10, 13]
    rl = 5
    RodCutting(l, p, rl).all_result()
