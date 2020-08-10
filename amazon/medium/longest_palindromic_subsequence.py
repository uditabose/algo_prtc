#!/usr/local/bin/python3
def is_palindrome(bstr):
    if not bstr:
        False

    if len(bstr) == 1:
        return True

    left, right = 0, len(bstr)-1
    while left < right:
        if bstr[left] != bstr[right] :
            return False

        left += 1
        right -= 1

    return True

def longest_palindromic_subsequence(astr):
    '''
    Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

    Example 1:
    Input:

    "bbbab"
    Output:
    4
    One possible longest palindromic subsequence is "bbbb".
    Example 2:
    Input:

    "cbbd"
    Output:
    2
    One possible longest palindromic subsequence is "bb".
    https://leetcode.com/problems/longest-palindromic-subsequence/description/

    Time :
    Space:
    Note :
    Idea is to keep the longest palindrome up until last character.
    '''
    if not astr:
        return 0

    palin_str = list(astr)
    max_palin = 1

    for last in range(1, len(astr)):
        for start in range(0, last):
            if is_palindrome(palin_str[start] + astr[last]):
                if (len(palin_str[last]) 
                    < len(palin_str[start] + astr[last])):
                    palin_str[last] = palin_str[start] + astr[last]
                    max_palin = max(max_palin, len(palin_str[last]))
    
    print(palin_str)
    return max_palin

def run():
    print(longest_palindromic_subsequence("bbbab"))
    print(longest_palindromic_subsequence("cbbd"))
    print(longest_palindromic_subsequence("cacbd"))
    print(longest_palindromic_subsequence("cac"))

if __name__ == '__main__':
    run()

