#!/usr/local/bin/python3

from typing import List


def left_right_array(nums: List[int]) -> List[int]:
    left_mult = [1 for i in nums]
    right_mult = [1 for i in nums]

    for i in range(1, len(nums)):
        left_mult[i] = left_mult[i-1] * nums[i-1]

    for j in range(len(nums) - 2, -1, -1):
        right_mult[j] = right_mult[j+1] * nums[j+1]

    result = []
    for i in range(0, len(nums)):
        result.append(left_mult[i] * right_mult[i])

    return result


def left_array(nums: List[int]) -> List[int]:
    left_mult = [1 for i in nums]
    for i in range(1, len(nums)):
        left_mult[i] = left_mult[i-1] * nums[i-1]

    result = [1 for i in nums]
    right_mult = 1
    for j in range(len(nums) - 1, -1, -1):
        result[j] = left_mult[j] * right_mult
        right_mult = right_mult * nums[j]

    return result


def product_of_array_except_self(nums: List[int]) -> List[int]:
    """
    https://leetcode.com/problems/product-of-array-except-self/

    Time :
    Space:
    Note :
    """
    if len(nums) < 2:
        return nums

    return (left_right_array(nums), left_array(nums))


def run():
    print(product_of_array_except_self([1, 2, 3, 4]))


if __name__ == '__main__':
    run()
