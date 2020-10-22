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
        


def three_sum_memo(nums: List[int]) -> List[List[int]]:

    two_sum_dict = {}

    for i in range(0, len(nums) - 2):



def three_sum(nums: List[int]) -> List[List[int]]:
    """
    https://leetcode.com/problems/3sum/

    Time :
    Space:
    Note :
    """
    if len(nums) < 3:
        return []

    return three_sum_brute(nums)


def run():
    print(three_sum([-1,0,1,2,-1,-4]))
    print("--------------")
    print(three_sum([]))
    print("--------------")
    print(three_sum([0]))
    print("--------------")


if __name__ == '__main__':
    run()
