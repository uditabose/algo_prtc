#!/usr/local/bin/python3

def make_power_set(num, power_set):
    new_elems = []
    for elem in power_set:
        if elem != None:
            telem = elem[:]
            telem.append(num)
            new_elems.append(sorted(telem))

    power_set.extend(new_elems)


def subsets(num_arr):
    """
    Given a set of distinct integers, nums, return
    all possible subsets (the power set).

    Note: The solution set must not contain duplicate subsets.

    Example:

    Input: nums = [1,2,3]
    Output:
    [
      [3],
      [1],
      [2],
      [1,2,3],
      [1,3],
      [2,3],
      [1,2],
      []
    ]
    https://leetcode.com/problems/subsets/description/

    Time :
    Space:
    Note :
    1.
    """
    if not num_arr:
        return []

    if len(num_arr) == 1:
        return [[], num_arr]

    power_set = [[]]

    for num in num_arr:
        make_power_set(num, power_set)
    return power_set


def run():
    print(subsets([1]))
    print(subsets([1, 2]))
    print(subsets([1, 2, 3]))
    print(subsets([1, 2, 3, 4]))


if __name__ == '__main__':
    run()
