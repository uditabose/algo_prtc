#!/usr/local/bin/python3
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        curr = self
        re = str(curr.val)
        while curr.next != None:
            re += "->" + str(curr.next.val)
            curr = curr.next

        return re

def make_list(arr):
    if len(arr) == 0:
        return
    root = ListNode(val = arr[0])
    prev = root
    for i in range(1, len(arr)):
        curr = ListNode(val = arr[i])
        prev.next = curr
        prev = curr

    return root

def merge_two_sorted_lists(list1, list2):
    """
    https://leetcode.com/problems/merge-two-sorted-lists/

    Time :
    Space:
    Note :
    """

    left = list1
    right = list2

    merged = None
    root = None
    while left != None and right != None:
        if left.val <= right.val:
            curr = left
            left = left.next
        else:
            curr = right
            right = right.next

        if merged == None:
            merged = curr
            root = merged
        else:
            merged.next = curr
            merged = merged.next

    if left != None:
        if merged == None:
            return left
        else:
            merged.next = left
    if right != None:
        if merged == None:
            return right
        else:
            merged.next = right
    return root

def run():
    arr1 = [1,2,4]
    arr2 = [1,3,4]
    list1 = make_list(arr1)
    list2 = make_list(arr2)
    print(list1, list2)
    print(merge_two_sorted_lists(list1, list2))


if __name__ == '__main__':
    run()
