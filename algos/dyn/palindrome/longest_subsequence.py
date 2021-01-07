from dynamic import Dynamic
from typing import List

# 2 cases
# variables : string, start, end
# 1: start and end character matches
#   a: return 2 + recurse with (start + 1, end - 1)
# 2: start and end character doesn't match
#   a: recurse with (start + 1, end)
#   b: recurse with (start, end - 1)
#   c: return the max(a, b)


class LongestSubsequence(Dynamic):
    def __init__(self, string: str):
        self.string = string

    def bruteforce(self):
        return LongestSubsequence.__recurse__(self.string, 0, len(self.string) - 1)

    @staticmethod
    def __recurse__(string: str, start: int, end: int):
        if len(string) == 0:
            return 0
        if start >= len(string) or end < 0:
            return 1
        if start == end:
            return 1
        if start > end:
            return 0

        if string[start] == string[end]:
            return 2 + LongestSubsequence.__recurse__(string, start + 1, end - 1)
        else:
            with_start = LongestSubsequence.__recurse__(string, start, end - 1)
            with_end = LongestSubsequence.__recurse__(string, start + 1, end)
            return max(with_start, with_end)

    def topdown(self):
        slen = len(self.string)
        memo = []
        for i in range(0, slen):
            memo.append([])
            for j in range(0, slen):
                if i == j:
                    memo[i].append(1)
                else:
                    memo[i].append(0)

        return LongestSubsequence.__recurse_memo__(self.string, 0, slen - 1, memo)

    @staticmethod
    def __recurse_memo__(string: str, start: int, end: int, memo: List[List[int]]):
        if len(string) == 0:
            return 0
        if start >= len(string) or end < 0:
            return 1
        if start == end:
            return 1
        if start > end:
            return 0

        if memo[start][end] > 0:
            return memo[start][end]

        if string[start] == string[end]:
            memo[start][end] = 2 + LongestSubsequence.__recurse_memo__(string, start + 1, end - 1, memo)
            return memo[start][end]
        else:
            memo[start][end - 1] = LongestSubsequence.__recurse_memo__(string, start, end - 1, memo)
            memo[start + 1][end] = LongestSubsequence.__recurse_memo__(string, start + 1, end, memo)
            return max(memo[start][end - 1], memo[start + 1][end])

    def bottomup(self):
        slen = len(self.string)
        table = []
        for i in range(0, slen):
            table.append([])
            for j in range(0, slen):
                if i == j:
                    table[i].append(1)
                else:
                    table[i].append(0)

        for i in range(slen - 1, -1, -1):
            for j in range(i + 1, slen):
                if self.string[i] == self.string[j]:
                    table[i][j] = 2 + table[i + 1][j - 1]
                else:
                    table[i][j] = max(table[i][j - 1], table[i + 1][j])

        return table[0][slen - 1]


if __name__ == '__main__':
    # LongestSubsequence("palindrome").all_result()
    LongestSubsequence("abdbca").all_result()
    # LongestSubsequence("cddpd").all_result()
    # LongestSubsequence("pqr").all_result()
