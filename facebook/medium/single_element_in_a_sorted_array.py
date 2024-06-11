#!/usr/local/bin/python3

from typing import List


def single_element_in_a_sorted_array(nums: List[int]) -> int:
    """
    https://leetcode.com/problems/single-element-in-a-sorted-array/

    Time :
    Space:
    Note :
    """
    if len(nums) == 1:
        return nums[0]

    ret = -1
    i = 0
    while i < len(nums) - 1:
        curr = nums[i]
        nxt = nums[i+1]
        if curr == nxt:
            i = i + 2
            ret = nums[i]
        else:
            ret = curr
            break
    return ret


def run():
    l = [1,1,2,3,3,4,4,8,8]
    single_element_in_a_sorted_array(l)
    l = [3,3,7,7,10,11,11]
    single_element_in_a_sorted_array(l)


if __name__ == '__main__':
    run()

