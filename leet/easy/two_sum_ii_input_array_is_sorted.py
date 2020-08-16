#!/usr/local/bin/python3

def two_sum_ii_input_array_is_sorted(nums, target):
    """
    https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

    Time :
    Space:
    Note :
    """
    left = 0
    right = 1
    while left < len(nums) - 1:
        if nums[left] + nums[right] == target:
            return [left + 1, right + 1]
        elif right == len(nums) - 1:
            left += 1
            right = left + 1
        else:
            right += 1


def run():
    nums = [2,7,11,15]
    target = 9
    print(two_sum_ii_input_array_is_sorted(nums, target))

    nums = [1,1,2,6]
    target = 8
    print(two_sum_ii_input_array_is_sorted(nums, target))

    target = 2
    print(two_sum_ii_input_array_is_sorted(nums, target))

    target = 3
    print(two_sum_ii_input_array_is_sorted(nums, target))

    target = 7
    print(two_sum_ii_input_array_is_sorted(nums, target))

    nums = [1,1]
    target = 2
    print(two_sum_ii_input_array_is_sorted(nums, target))


if __name__ == '__main__':
    run()
