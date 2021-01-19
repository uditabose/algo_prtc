from dynamic import Dynamic
from typing import List


class CountSubstring(Dynamic):
    def __init__(self, string):
        self.string = string

    def bruteforce(self):
        return CountSubstring.__recurse__(self.string, 0, len(self.string) - 1)

    @staticmethod
    def __is_palindrome__(string: str, start: int, end: int):
        if start > end:
            return False
        if start == end:
            return True

        if string[start] == string[end]:
            if start + 1 == end:
                return True
            return CountSubstring.__is_palindrome__(string, start + 1, end - 1)
        return False

    @staticmethod
    def __recurse__(string, start, end):
        if start > end:
            return 0

        if CountSubstring.__is_palindrome__(string, start, end):
            return 1 + CountSubstring.__recurse__(string, start + 1, end - 1)
        return CountSubstring.__recurse__(string, start + 1, end) \
               + CountSubstring.__recurse__(string, start, end - 1)

    def topdown(self):
        slen = len(self.string)
        memo = [[-1 for _ in range(slen)] for _ in range(slen)]
        return CountSubstring.__recurse_memo__(self.string, 0, slen - 1, memo)

    @staticmethod
    def __recurse_memo__(string, start, end, memo):
        if start > end:
            return 0
        if start == end:
            memo[start][end] = 1

        if memo[start][end] > -1:
            return memo[start][end]

        if CountSubstring.__is_palindrome__(string, start, end):
            memo[start][end - 1] = 1 + CountSubstring.__recurse_memo__(string, start + 1, end - 1, memo)

        memo[start][end - 1] = CountSubstring.__recurse_memo__(string, start, end - 1, memo)
        memo[start + 1][end] = CountSubstring.__recurse_memo__(string, start + 1, end, memo)

        print(memo)
        return memo[start][end]

    def bottomup(self):
        slen = len(self.string)
        table = [[False for _ in range(slen)] for _ in range(slen)]

        palin_count = 0
        for i in range(slen):
            table[i][i] = True
            palin_count += 1

        for start in range(slen - 1, -1, -1):
            for end in range(start + 1, slen):
                if self.string[start] == self.string[end]:
                    if end - start == 1 or table[start + 1][end - 1]:
                        table[start][end] = True
                        palin_count += 1

        return palin_count


if __name__ == '__main__':
    # print(CountSubstring.__is_palindrome__("a", 0, 0))
    # print(CountSubstring.__is_palindrome__("aa", 0, 1))
    # print(CountSubstring.__is_palindrome__("aaa", 0, 2))
    # print(CountSubstring.__is_palindrome__("aba", 0, 2))
    # print(CountSubstring.__is_palindrome__("abba", 0, 3))
    # print(CountSubstring.__is_palindrome__("abca", 0, 3))
    CountSubstring("abdbca").all_result()
