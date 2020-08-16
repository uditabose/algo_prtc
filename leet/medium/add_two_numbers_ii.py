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


def get_num(root):
    if root == None or root.val == None:
        return 0

    num = -1
    curr = root
    while curr != None:
        cur_num = int(curr.val)
        if num == -1:
            num = cur_num
        else:
            num = num * 10 + cur_num
        curr = curr.next

    return num

def do_list(num):
    num_str = str(num)
    root = ListNode(val = int(num_str[0]))
    curr = root
    for i in range(1, len(num_str)):
        curr.next = ListNode(val = num_str[i])
        curr = curr.next

    return root


def add_two_numbers_ii(l1, l2):
    """
    https://leetcode.com/problems/add-two-numbers-ii/

    Time :
    Space:
    Note :
    """

    num1 = get_num(l1)
    num2 = get_num(l2)

    return num1 + num2

def run():
    arr1 = [7,2,4,3]
    arr2 = [5,6,4]
    list1 = make_list(arr1)
    list2 = make_list(arr2)

    print(do_list(add_two_numbers_ii(list1, list2)))



if __name__ == '__main__':
    run()
