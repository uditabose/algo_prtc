#!/usr/local/bin/python3
from typing import List

def running_sum_of_1d_array(nums: List[int]) -> List[int]:
    """
    https://leetcode.com/problems/running-sum-of-1d-array/submissions/

    Time :
    Space:
    Note :
    """
    for i, n in enumerate(nums):
        if i == 0:
            continue
        else:
            nums[i] = nums[i-1] + n
    return nums


def run():
    print(running_sum_of_1d_array([1, 2, 3]))


if __name__ == '__main__':
    run()
