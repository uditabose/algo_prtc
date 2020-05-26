
####
# Given a sequence, find the length of its Longest Palindromic Subsequence (LPS).
# In a palindromic subsequence, elements read the same backward and forward.
# https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/RMk1D1DY1PL
####

#### Start Brute-force ####

def recurse_longest_palindrome(palin_string, start_idx, end_idx):
    if len(palin_string) == 1:
        return 1

    if start_idx >= end_idx:
        return 1

    if palin_string[start_idx] == palin_string[end_idx]:
        return 2 + recurse_longest_palindrome(palin_string, start_idx + 1, end_idx - 1)
    else:
        len_with_start = recurse_longest_palindrome(palin_string, start_idx, end_idx - 1)
        len_with_end = recurse_longest_palindrome(palin_string, start_idx + 1, end_idx)
        return max(len_with_start, len_with_end)

def brute_longest_palindrome(palin_string):
    len_st = len(palin_string)
    # trivial case: input string length is 0 or 1
    if len_st < 2:
        return len_st

    return recurse_longest_palindrome(palin_string, 0, len_st - 1)
#### End Brute-force ####

#### Start Memoized ####

def memo_recurse_longest_palindrome(memo, palin_string, start_idx, end_idx):
    if len(palin_string) == 1:
        return 1

    if start_idx >= end_idx:
        return 1

    if memo[start_idx][end_idx] != -1:
        return memo[start_idx][end_idx]

    if palin_string[start_idx] == palin_string[end_idx]:
        memo[start_idx][end_idx] = 2 + memo_recurse_longest_palindrome(memo, palin_string, start_idx + 1, end_idx - 1)
    else:
        len_with_start = memo_recurse_longest_palindrome(memo, palin_string, start_idx, end_idx - 1)
        len_with_end = memo_recurse_longest_palindrome(memo, palin_string, start_idx + 1, end_idx)
        memo[start_idx][end_idx] = max(len_with_start, len_with_end)

    return memo[start_idx][end_idx]


def memoized_longenst_palindrome(palin_string):
    len_st = len(palin_string)
    # trivial case: input string length is 0 or 1
    if len_st < 2:
        return len_st

    memo = [[-1 for _ in range(len_st)] for _ in range(len_st)]

    return memo_recurse_longest_palindrome(memo, palin_string, 0, len_st - 1)

#### End Memoized ####

#### Start Tabulated ####
def tabulated_longenst_palindrome(palin_string):
    len_st = len(palin_string)
    # trivial case: input string length is 0 or 1
    if len_st < 2:
        return len_st

    table = [[0 for _ in range(len_st)] for _ in range(len_st)]
    for i in range(len_st):
        table[i][i] = 1

    for start_idx in range(len_st - 1, -1, -1):
        for end_idx in range(start_idx + 1, len_st):
            if palin_string[start_idx] == palin_string[end_idx]:
                table[start_idx][end_idx] = 2 + table[start_idx + 1][end_idx - 1]
            else:
                table[start_idx][end_idx] = max(table[start_idx][end_idx - 1], table[start_idx + 1][end_idx])


    return table[0][len_st - 1]
#### End Tabulated ####

def main():
    input = "abdbca"
    print("longest palindrome length of '%s' is %i" % (input, brute_longest_palindrome(input)))

    input = "cddpd"
    print("longest palindrome length of '%s' is %i" % (input, brute_longest_palindrome(input)))

    input = "pqr"
    print("longest palindrome length of '%s' is %i" % (input, brute_longest_palindrome(input)))

    print("----------------")

    input = "abdbca"
    print("longest palindrome length of '%s' is %i" % (input, memoized_longenst_palindrome(input)))

    input = "cddpd"
    print("longest palindrome length of '%s' is %i" % (input, memoized_longenst_palindrome(input)))

    input = "pqr"
    print("longest palindrome length of '%s' is %i" % (input, memoized_longenst_palindrome(input)))

    print("----------------")

    input = "abdbca"
    print("longest palindrome length of '%s' is %i" % (input, tabulated_longenst_palindrome(input)))

    input = "cddpd"
    print("longest palindrome length of '%s' is %i" % (input, tabulated_longenst_palindrome(input)))

    input = "pqr"
    print("longest palindrome length of '%s' is %i" % (input, tabulated_longenst_palindrome(input)))


if __name__ == "__main__":
    main()
