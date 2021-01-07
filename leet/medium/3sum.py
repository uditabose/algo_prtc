#!/usr/local/bin/python3

from typing import List


def three_sum_brute(nums: List[int]) -> List[List[int]]:
    zero_sum = set()
    for i in range(0, len(nums) - 2):
        for j in range(i+1, len(nums) - 1):
            for k in range(j+1, len(nums)):
                if (nums[i] + nums[j] + nums[k]) == 0:
                    zero_sum.add(tuple(sorted([nums[i], nums[j], nums[k]])))

    return list(zero_sum)


def two_sum(nums, exclude, target):
    num_set = set(nums)
    for i in range(0, len(nums)):
        if i == exclude:
            continue
        if target - nums[i] in num_set:
            return (nums[i], target - nums[i])


def three_sum_memo(nums: List[int]) -> List[List[int]]:

    three_sum = set()
    for i in range(0, len(nums) - 2):
        ts = two_sum(nums, i, (-1) * nums[i])
        three_sum.add((nums[i], ts[0], ts[1]))

    return list(three_sum)


def run():
    """
    https://leetcode.com/problems/3sum/

    Time :
    Space:
    Note :
    """
    print(three_sum_brute([-1, 0, 1, 2, -1, -4]))
    print("--------------")
    print(three_sum_brute([]))
    print("--------------")
    print(three_sum_brute([0]))
    print("--------------")
    print("===============")
    print(three_sum_memo([-1, 0, 1, 2, -1, -4]))
    print("--------------")
    print(three_sum_memo([]))
    print("--------------")
    print(three_sum_memo([0]))
    print("--------------")


if __name__ == '__main__':
    run()
