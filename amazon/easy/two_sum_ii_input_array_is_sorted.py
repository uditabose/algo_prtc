#!/usr/local/bin/python3

def two_sum_ii_input_array_is_sorted(num_arr, expected):
    """
    Given an array of integers that is already
    sorted in ascending order, find two numbers such
    that they add up to a specific target number.

    The function twoSum should return indices of the
    two numbers such that they add up to the target,
    where index1 must be less than index2.

    Note:

    Your returned answers (both index1 and index2) are
    not zero-based.
    You may assume that each input would have exactly
    one solution and you may not use the same element twice.
    Example:

    Input: numbers = [2,7,11,15], target = 9
    Output: [1,2]
    Explanation: The sum of 2 and 7 is 9.
    Therefore index1 = 1, index2 = 2.

    https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

    Time :
    Space:
    Note :
    1. two indices, left and right end
    2. sum end values, if sum > expected,
        move right one step left
    3. otherwise, move left to one step to right
    4. if sum == expected, return indices
    """
    if (not num_arr) or len(num_arr) < 2:
        return None

    left, right = 0, len(num_arr) - 1

    while left < right:
        summed = num_arr[left] + num_arr[right]
        if summed == expected:
            return [left+1, right+1]
        elif summed > expected:
            right -= 1
        else:
            left += 1

    if num_arr[left] + num_arr[right] == expected:
        return [left+1, right+1]
    else:
        return None

def run():
    num_arr = [2,7,11,15]
    expected = 9
    print(two_sum_ii_input_array_is_sorted(num_arr, expected))

if __name__ == '__main__':
    run()
