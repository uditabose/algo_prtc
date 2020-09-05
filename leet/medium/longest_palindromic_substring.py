#!/usr/local/bin/python3

def is_palindrome(s: str, start: int, end: int):
    if start == end:
        return True
    elif start >= end:
        return False
    elif s[start] != s[end]:
        return False
    else:
        if start + 1 == end:
            return True
        else:
            return is_palindrome(s, start + 1, end - 1)


def longest_palindromic_substring_memo(s: str) -> str:
    if len(s) < 2:
        return s

    if len(s) == 2:
        return s if s[0] == s[1] else s[0]

    memo = [ [ None for j in range(0, len(s)) ] for i in range(0, len(s)) ]
    for i in range(0, len(s)):
        memo[i][i] = s[i]

    max_palindrome = ""
    for i in range(0, len(s)):
        for j in range(len(s) - 1, i, -1):
            if memo[i][j] != None:
                max_palindrome = max(max_palindrome, memo[i][j])
            elif is_palindrome(s, i, j):
                memo[i][j] = s[i:j + 1]
                max_palindrome = max(max_palindrome, memo[i][j])

    return max_palindrome


def longest_palindromic_substring_brute(s: str) -> str:
    if len(s) < 2:
        return s

    if len(s) == 2:
        return s if s[0] == s[1] else s[0]

    max_palindrome = ""

    for i in range(0, len(s)):
        for j in range(len(s) - 1, i, -1):
            if is_palindrome(s, i, j):
                max_palindrome = max(max_palindrome, s[i:j + 1])

    return max_palindrome

def run():
    """
    https://leetcode.com/problems/longest-palindromic-substring/

    Time :
    Space:
    Note :
    """
    print(longest_palindromic_substring_brute("babad"))
    print(longest_palindromic_substring_brute("cbbd"))

    print(longest_palindromic_substring_memo("babad"))
    print(longest_palindromic_substring_memo("cbbd"))



if __name__ == '__main__':
    run()
