#!/usr/local/bin/python3

from typing import List


def next_permutation(nums: List[int]) -> None:
    """
    https://leetcode.com/problems/next-permutation/

    Time :
    Space:
    Note :
    """
    if len(nums) < 2:
        return nums

    right_idx = - 1
    for j in range(len(nums) - 1, -1, -1):
        if nums[j - 1] < nums[j]:
            right_idx = j
            break

    if right_idx == -1:
        nums = reversed(nums)
    else:
        nums[1], nums[right_idx] = nums[right_idx], nums[1]

    return list(nums)


def run():
    print(next_permutation([1, 2, 3]))
    print(next_permutation([3, 2, 1]))
    print(next_permutation([1, 1, 5]))
    print(next_permutation([7, 1, 8, 2, 5, 4]))


if __name__ == '__main__':
    run()
