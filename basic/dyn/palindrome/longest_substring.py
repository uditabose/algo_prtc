from dynamic import Dynamic
from typing import List

# 2 cases
# variables : string, start, end
# 1: start and end character matches
#   a: find if substring (start + 1, end - 1) is palindrome
#   b: if yes, max length is (end - start + 1)
#   c: else, return 0
# 2: start and end character doesn't match
#   a: find if substring (start + 1, end) is palindrome
#   b: find if substring (start, end - 1) is palindrome
#   c: return the max(a, b)


class LongestSubstring(Dynamic):
    def __init__(self, string: str):
        self.string = string

    def bruteforce(self):
        return LongestSubstring.__recurse__(self.string, 0, len(self.string) - 1)



    @staticmethod
    def __recurse__(string: str, start: int, end: int):
        if start > end:
            return 0

        if start == end:
            return 1

        if string[start] == string[end]:
            max_len = end - start - 1
            if LongestSubstring.__recurse__(string, start + 1, end - 1) == max_len:
                return max_len + 2

        with_start = LongestSubstring.__recurse__(string, start, end - 1)
        with_out_start = LongestSubstring.__recurse__(string, start + 1, end)
        return max(with_start, with_out_start)

    def topdown(self):
        slen = len(self.string)
        memo = [[-1 for _ in range(slen)] for _ in range(slen)]
        return LongestSubstring.__recurse_memo__(self.string, 0, slen - 1, memo)

    @staticmethod
    def __recurse_memo__(string: str, start: int, end: int, memo: List[List[int]]):
        if start > end:
            return 0

        if start == end:
            return 1

        if memo[start][end] != -1:
            return memo[start][end]

        if string[start] == string[end]:
            max_len = end - start - 1
            if LongestSubstring.__recurse_memo__(string, start + 1, end - 1, memo) == max_len:
                memo[start][end] = max_len + 2

        with_start = LongestSubstring.__recurse__(string, start, end - 1)
        with_out_start = LongestSubstring.__recurse__(string, start + 1, end)
        memo[start][end] = max(with_start, with_out_start)
        return memo[start][end]

    def bottomup(self):
        slen = len(self.string)
        table = [[False for _ in range(slen)] for _ in range(slen)]
        for i in range(slen):
            table[i][i] = True

        max_len = 1
        for start in range(slen - 1, -1, -1):
            for end in range(start + 1, slen):
                if self.string[start] == self.string[end] and table[start + 1][end - 1]:
                    table[start][end] = True
                    max_len = max(max_len, end - start + 1)

        return max_len


if __name__ == '__main__':
    LongestSubstring("abdbca").all_result()
