#!/usr/local/bin/python3

def two_sum_two_pointers(nums, target):
    """
    https://leetcode.com/problems/two-sum/

    Time :
    Space:
    Note :
    """
    left = 0
    right = 1
    while left < len(nums) - 1:
        if nums[left] + nums[right] == target:
            return [left, right]
        elif right == len(nums) - 1:
            left += 1
            right = left + 1
        else:
            right += 1

def two_sum_hash(nums, target):
    """
    https://leetcode.com/problems/two-sum/

    Time :
    Space:
    Note :
    """
    num_hash = {}
    for i, n in enumerate(nums):
        num_hash[n] = i

    for i, n in enumerate(nums):
        diff = target - n
        if diff in num_hash:
            return [i, num_hash[diff]]

def run():
    nums = [2, 7, 11, 15]
    target = 22
    print(two_sum_hash(nums, target))
    print(two_sum_two_pointers(nums, target))


if __name__ == '__main__':
    run()
