from dynamic import Dynamic
from typing import List

class HouseThief(Dynamic):
    def __init__(self, wealth_list: List[int]):
        self.wealth_list = wealth_list

    def bruteforce(self):
        return HouseThief.__recurse__(self.wealth_list, 0)

    @staticmethod
    def __recurse__(wealth_list: List[int], start: int):
        if start >= len(wealth_list):
            return 0

        steal_with_start = wealth_list[start] + HouseThief.__recurse__(wealth_list, start + 2)
        steal_without_start = HouseThief.__recurse__(wealth_list, start + 1)

        return max(steal_with_start, steal_without_start)

    def topdown(self):
        memo = [0 for i in self.wealth_list]
        return HouseThief.__recurse_memo__(self.wealth_list, 0, memo)

    @staticmethod
    def __recurse_memo__(wealth_list: List[int], start: int, memo: List[int]):
        if start >= len(wealth_list):
            return 0

        if memo[start] == 0:
            steal_with_start = wealth_list[start] + HouseThief.__recurse_memo__(wealth_list, start + 2, memo)
            steal_without_start = HouseThief.__recurse_memo__(wealth_list, start + 1, memo)
            memo[start] = max(steal_with_start, steal_without_start)
        # print(memo)
        return memo[start]

    def bottomup(self):
        table = [0 for i in range(len(self.wealth_list) + 1)]
        table[0] = 0
        table[1] = self.wealth_list[0]
        for i in range(1, len(self.wealth_list)):
            table[i + 1] = max(self.wealth_list[i] + table[i - 1], table[i])

        # print(table)
        return table[-1]


if __name__ == '__main__':
    HouseThief([2, 10, 14, 8, 1]).all_result()
