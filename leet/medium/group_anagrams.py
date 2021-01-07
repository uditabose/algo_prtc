#!/usr/local/bin/python3
from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    https://leetcode.com/problems/group-anagrams/

    Time :
    Space:
    Note :
    """
    if len(strs) < 2:
        return [strs]

    anagram_map = {}
    for word in strs:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_map:
            anagram_map[sorted_word].append(word)
        else:
            anagram_map[sorted_word] = [word]

    return list(anagram_map.values())


def run():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(group_anagrams(strs))

    strs = [""]
    print(group_anagrams(strs))

    strs = ["a"]
    print(group_anagrams(strs))


if __name__ == '__main__':
    run()
