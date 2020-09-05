#!/usr/local/bin/python3
from typing import List

def rotate_array(nums: List[int], k: int):
    """
    https://leetcode.com/problems/rotate-array/

    Time :
    Space:
    Note :
    """
    if len(nums) < 2:
        return nums

    from_idx = swapped_val_idx = 0
    times_swapped = 0
    while times_swapped < len(nums):
        if from_idx < k:
            to_idx = from_idx + k
        else:
            to_idx = from_idx + k - len(nums)

        nums[to_idx], nums[from_idx] = nums[swapped_val_idx], nums[to_idx]
        swapped_val_idx = to_idx
        from_idx = to_idx
        times_swapped += 1

    print(nums)

def run():
    rotate_array([1,2,3,4,5,6,7], 3)
    rotate_array([-1,-100,3,99], 2)


if __name__ == '__main__':
    run()
