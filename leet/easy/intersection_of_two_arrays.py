#!/usr/local/bin/python3

def intersection_of_two_arrays(nums1, nums2):
    """
    https://leetcode.com/problems/intersection-of-two-arrays/

    Time :
    Space:
    Note :
    """
    if nums1 == None or nums2 == None:
        return []

    itersection = {}
    num_set = {n: None for n in nums1}
    for n in nums2:
        if n in num_set and n not in itersection:
            itersection[n] = None

    return list(itersection)


def run():
    arr1 = [1,2,2,1]
    arr2 = [2,2]

    print(intersection_of_two_arrays(arr1, arr2))

    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    print(intersection_of_two_arrays(nums1, nums2))


if __name__ == '__main__':
    run()
