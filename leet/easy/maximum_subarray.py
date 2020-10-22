#!/usr/local/bin/python3

from typing import List

def maximum_subarray(nums: List[int]) -> int:
    """
    https://leetcode.com/problems/maximum-subarray/

    Time :
    Space:
    Note :
    """
    if len(nums) == 0:
        return 0

    if len(nums) == 1:
        return nums[0]

    max_cont_sum_till = [None for i in range(0, len(nums))]
    max_sum = None
    for idx, num in enumerate(nums):
        if idx == 0:
            max_cont_sum_till[idx] = num
            max_sum = num
        else:
            sum_till_current = max_cont_sum_till[idx - 1] + num
            if sum_till_current > num:
                max_cont_sum_till[idx] = sum_till_current
            else:
                max_cont_sum_till[idx] = num

            max_sum = max(max_sum, max_cont_sum_till[idx])

    return max_sum


def run():
    print(maximum_subarray([-1,1,-1]))
    print(maximum_subarray([-1,0]))
    print(maximum_subarray([-1,-1]))
    print(maximum_subarray([-1,1]))
    print(maximum_subarray([1,1]))
    print(maximum_subarray([1,-1]))
    print(maximum_subarray([-1,-1,-1]))
    print(maximum_subarray([1,1,1]))
    print(maximum_subarray([5,4,3,2,1]))
    print(maximum_subarray([1,2,3,4,5]))
    print(maximum_subarray([-2147483647]))
    print(maximum_subarray([-2,1,-3,4,-1,2,1,-5,4]))


if __name__ == '__main__':
    run()
