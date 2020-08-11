#!/usr/local/bin/python3

def longest_substring_without_repeating_characters_bf(s: str) -> int:
    """
    https://leetcode.com/problems/longest-substring-without-repeating-characters/

    Time : O(N^2)
    Space: O(1)
    Note :
    """
    i = 0
    max_substring_length = 1
    while i < len(s) - 1:

        j = i + 1
        curr_ch = s[i]
        char_set = {}
        char_set[curr_ch] = None
        while j < len(s):
            if s[j] in char_set:
                break
            else:
                char_set[s[j]] = None
                j += 1
            max_substring_length = max(max_substring_length, (j-i))

        i += 1

    return max_substring_length


def longest_substring_without_repeating_characters(s: str) -> int:
    """
    https://leetcode.com/problems/longest-substring-without-repeating-characters/

    Time : O(N)
    Space: O(N)
    Note :
    """
    if len(s) < 2:
        return len(s)

    i = 0
    left = 0
    char_set = {}
    max_substring_length = 1
    while i < len(s):
        if s[i] in char_set:
            max_substring_length = max(max_substring_length, len(char_set))
            left += 1
            i = left
            char_set.clear()
        else:
            char_set[s[i]] = None
            i += 1

    max_substring_length = max(max_substring_length, len(char_set))
    return max_substring_length


def run():
    strings = ["bbbbb"]
    #["abcabcbb", "dvdf", "pwwkew", "anviaj", "bbbbb"]
    # for st in strings:
    #     print(f"{st} :: {longest_substring_without_repeating_characters_bf(st)}")
    #

    for st in strings:
        print(f"{st} :: {longest_substring_without_repeating_characters(st)}")

if __name__ == '__main__':
    run()
