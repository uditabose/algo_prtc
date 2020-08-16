#!/usr/local/bin/python3

def two_sum_two_pointers(nums, target, ex):
    left = 0
    right = 1
    while left < len(nums) - 1:
        if left == ex:
            left += 1
            continue
        if right == ex:
            right += 1
            continue
        if left == right:
            right += 1
        if right >= len(nums):
            return

        if nums[left] + nums[right] == target:
            return [left, right]
        elif right == len(nums) - 1:
            left += 1
            right = left + 1
        else:
            right += 1

def three_sum(nums):
    """
    https://leetcode.com/problems/3sum/

    Time :
    Space:
    Note :
    """
    result = []
    for i in range(0, len(nums) - 2):
        two_sums = two_sum_two_pointers(nums, (-1) * nums[i], i + 1)
        if two_sums != None:
            result.append([nums[i], nums[two_sums[0]], nums[two_sums[1]]])

    return result


def run():
    nums =  [-1, 0, 1, 2, -1, -4]
    print(three_sum(nums))


if __name__ == '__main__':
    run()
