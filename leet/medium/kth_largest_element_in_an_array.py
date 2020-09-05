#!/usr/local/bin/python3



def kth_largest_element_in_an_array_heap(nums, k):
    """
    https://leetcode.com/problems/kth-largest-element-in-an-array/

    Time : O(nlogk)
    Space:
    Note :
    """


    return nums[k]

def kth_largest_element_in_an_array_sort(nums, k):
    """
    https://leetcode.com/problems/kth-largest-element-in-an-array/

    Time : O(nlogn)
    Space:
    Note :
    """
    return heapq.nlargest(k, nums)


def run():
    pass


if __name__ == '__main__':
    run()
