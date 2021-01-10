from dynamic import Dynamic
from typing import List


class NumberFactor(Dynamic):
    def __init__(self, number: int):
        self.number = number

    def bruteforce(self):
        return NumberFactor.__recurse__(self.number)

    @staticmethod
    def __recurse__(n: int):
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 1
        if n == 3:
            return 2

        n_1 = NumberFactor.__recurse__(n - 1)
        n_3 = NumberFactor.__recurse__(n - 3)
        n_4 = NumberFactor.__recurse__(n - 4)

        return n_1 + n_3 + n_4

    def topdown(self):
        memo = [-1 for i in range(0, self.number + 1)]
        memo[0] = 1
        memo[1] = 1
        memo[2] = 1
        memo[3] = 2

        return NumberFactor.__recurse_memo__(self.number, memo)

    @staticmethod
    def __recurse_memo__(n: int, memo: List[int]):
        if memo[n] > -1:
            return memo[n]

        memo[n] = NumberFactor.__recurse_memo__(n - 1, memo) \
                  + NumberFactor.__recurse_memo__(n - 3, memo) \
                  + NumberFactor.__recurse_memo__(n - 4, memo)
        return memo[n]

    def bottomup(self):
        table = [-1 for i in range(0, self.number + 1)]
        table[0] = 1
        table[1] = 1
        table[2] = 1
        table[3] = 2

        for i in range(4, self.number + 1):
            table[i] = table[i - 1] + table[i - 3] + table[i - 4]

        return table[self.number]


if __name__ == '__main__':
    number_factor = NumberFactor(5)
    number_factor.all_result()
