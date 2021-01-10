from dynamic import Dynamic
from typing import List
import math


class MinJumpsToEnd(Dynamic):
    def __init__(self, jump_list: List[int]):
        self.jump_list = jump_list

    def bruteforce(self):
        return MinJumpsToEnd.__recurse__(self.jump_list, 0)

    @staticmethod
    def __recurse__(jump_list: List[int], jump_point: int):
        if len(jump_list) == 0:
            return 0
        if jump_point >= len(jump_list) - 1:
            return 0
        if jump_list[jump_point] == 0:
            return math.inf

        total_jumps = math.inf
        max_jump = jump_list[jump_point]
        current = 1
        while current <= max_jump:
            jump_count = MinJumpsToEnd.__recurse__(jump_list, current + jump_point)
            if jump_count != math.inf:
                total_jumps = min(total_jumps, jump_count + 1)
            current += 1

        return total_jumps

    def topdown(self):
        memo = [math.inf for i in self.jump_list]
        return MinJumpsToEnd.__recurse_memo__(self.jump_list, 0, memo)

    @staticmethod
    def __recurse_memo__(jump_list: List[int], jump_point: int, memo: List[float]):
        if len(jump_list) == 0:
            return 0
        if jump_point >= len(jump_list) - 1:
            return 0
        if jump_list[jump_point] == 0:
            return math.inf
        if memo[jump_point] != math.inf:
            return memo[jump_point]

        max_jump = jump_list[jump_point]
        current = 1
        while current <= max_jump:
            jump_count = MinJumpsToEnd.__recurse_memo__(jump_list, current + jump_point, memo)
            if jump_count != math.inf:
                memo[jump_point] = min(memo[jump_point], jump_count + 1)
            current += 1

        return memo[jump_point]

    def bottomup(self):
        l = len(self.jump_list)
        if l < 2:
            return 0

        table = [math.inf for i in self.jump_list]
        table[-1] = 0
        jump_point = l - 2

        while jump_point >= 0:
            max_jump = self.jump_list[jump_point]

            # opposed to other 2 approaches, here we start from behind
            # filling out the table from end
            current = 1
            while current <= max_jump:
                if jump_point + current < l:
                    table[jump_point] = min(table[jump_point], table[jump_point + current] + 1)
                current += 1
            jump_point -= 1
        return table[0]


if __name__ == '__main__':
    # jumps = [2, 1, 1, 1, 4]
    jumps = [1, 1, 3, 6, 9, 3, 0, 1, 3]
    min_jumps = MinJumpsToEnd(jumps)
    min_jumps.all_result()
