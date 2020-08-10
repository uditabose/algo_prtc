class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        lstr = ""
        curr = self
        while curr != None:
            lstr += str(curr.val)
            lstr += " > "
            curr = curr.next

        return lstr

def reverse_nodes_in_k_group(alist, grp):
    '''
    Given a linked list, reverse the nodes of 
    a linked list k at a time and return its modified list.

    k is a positive integer and is less than or 
    equal to the length of the linked list. If the 
    number of nodes is not a multiple of k then left-out 
    nodes in the end should remain as it is.

    Example:
    Given this linked list: 1->2->3->4->5
    For k = 2, you should return: 2->1->4->3->5
    For k = 3, you should return: 3->2->1->4->5

    Only constant extra memory is allowed.
    You may not alter the values in the list's nodes, 
    only nodes itself may be changed.
    https://leetcode.com/problems/reverse-nodes-in-k-group/description/

    Time : O(N)
    Space: O(1)
    Note :
    '''
    if alist == None or len(alist) == 0:
        return alist

    if grp < 2 or grp >= len(alist):
        return alist

    st_pos = 0
    while True:
        left = st_pos
        right = left + grp - 1
        #print("%d - %d" % (left, right))
        if right >= len(alist):
            break
        while left < right:
            alist[left], alist[right] = alist[right], alist[left]
            left += 1
            right -= 1
            #print(alist)
        st_pos += grp

def run():
    num_arr = [1, 2, 3, 4, 5]
    #print(num_arr)
    reverse_nodes_in_k_group(num_arr, 2)
    print(num_arr)
    print("--------------")

    num_arr = [1, 2, 3, 4, 5]
    #print(num_arr)
    reverse_nodes_in_k_group(num_arr, 3)
    print(num_arr)
    print("--------------")

if __name__ == '__main__':
    run()

