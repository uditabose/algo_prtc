#!/usr/local/bin/python3

def longest_substring_with_at_most_two_distinct_characters(s: str) -> int:
    """
    https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/

    Time :
    Space:
    Note :
    """

    if len(s) <= 2:
        return len(s)

    i = 0
    left = 0
    char_set = {}
    max_substring_length = 1
    while i < len(s):
        char_set[s[i]] = None
        if len(char_set) == 3:
            max_substring_length = max(max_substring_length, i - left)
            left += 1
            i = left
            char_set.clear()
        else:
            i += 1

    max_substring_length = max(max_substring_length, len(s) - left)
    return max_substring_length



def run():
    strings = ["ab", "eceba"]
    #["abcabcbb", "dvdf", "pwwkew", "anviaj", "bbbbb"]
    # for st in strings:
    #     print(f"{st} :: {longest_substring_without_repeating_characters_bf(st)}")
    #

    for st in strings:
        print(f"{st} :: {longest_substring_with_at_most_two_distinct_characters(st)}")



if __name__ == '__main__':
    run()
