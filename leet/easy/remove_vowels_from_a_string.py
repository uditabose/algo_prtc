#!/usr/local/bin/python3

def remove_vowels_from_a_string(S):
    """
    https://leetcode.com/problems/remove-vowels-from-a-string/

    Time :
    Space:
    Note :
    """
    formatted_str = []
    for ch in S:
        if ch not in "aeiou":
            formatted_str.append(ch)
    return ''.join(formatted_str)


def run():
    print(remove_vowels_from_a_string("leetcodeisacommunityforcoders"))


if __name__ == '__main__':
    run()
