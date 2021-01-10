from dynamic import Dynamic
from typing import List
import math


class MinJumpWithFee(Dynamic):
    def __init__(self, jump_fee: List[int]):
        self.jump_fee = jump_fee

    def bruteforce(self):
        return MinJumpWithFee.__recurse__(self.jump_fee, 0)

    @staticmethod
    def __recurse__(jump_fee: List[int], jump_point: int):
        if jump_point >= len(jump_fee) - 1:
            return 0

        min_fee = min(
            MinJumpWithFee.__recurse__(jump_fee, jump_point + 1),
            MinJumpWithFee.__recurse__(jump_fee, jump_point + 2),
            MinJumpWithFee.__recurse__(jump_fee, jump_point + 3)
        )

        min_fee += jump_fee[jump_point]

        # print("point : {} - fee {}".format(jump_point, min_fee))
        return min_fee

    def topdown(self):
        memo = [0 for n in range(0, len(self.jump_fee) + 1)]
        return MinJumpWithFee.__recurse_memo__(self.jump_fee, 0, memo)

    @staticmethod
    def __recurse_memo__(jump_fee: List[int], jump_point: int, memo: List[float]):
        if jump_point >= len(jump_fee) - 1:
            return 0
        if memo[jump_point] != 0:
            return memo[jump_point]

        min_fee = min(
            MinJumpWithFee.__recurse_memo__(jump_fee, jump_point + 1, memo),
            MinJumpWithFee.__recurse_memo__(jump_fee, jump_point + 2, memo),
            MinJumpWithFee.__recurse_memo__(jump_fee, jump_point + 3, memo)
        )
        memo[jump_point] = jump_fee[jump_point] + min_fee
        return memo[jump_point]

    def bottomup(self):
        jl = len(self.jump_fee)
        table = [0 for n in range(0, jl + 1)]
        table[1] = self.jump_fee[0]
        table[2] = self.jump_fee[0]

        for current in range(2, jl - 1):
            n_1 = self.jump_fee[current - 1] + table[current - 1]
            n_2 = self.jump_fee[current - 2] + table[current - 2]
            n_3 = self.jump_fee[current - 3] + table[current - 3]
            table[current + 1] = min(n_1, n_2, n_3)

        return table[jl - 1]


if __name__ == '__main__':
    # jumps = [1, 2, 5, 2, 1, 2]
    jumps = [2, 3, 4, 5]
    MinJumpWithFee(jumps).all_result()
