
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

def find_min(list_ln): # O(m)
    if not list_ln or len(list_ln) == 0:
        return None
    print(list_ln)
    
    minnode = list_ln[0]
    minpos = 0
    for pos, node in enumerate(list_ln):
        if node and minnode and node.val < minnode.val:
            minnode = node
            minpos = pos
    if minnode:
        list_ln[minpos] = minnode.next
    clean_empty_elems(list_ln)
    print(list_ln)
    return minnode

def clean_empty_elems(list_ln):
    lenn = len(list_ln) - 1
    while lenn >= 0:
        if list_ln[lenn] == None:
            del list_ln[lenn]
            lenn -= 2
        else:
            lenn -= 1
        
def merge_k_sorted_lists(lists):
    '''
    Merge k sorted linked lists and return it as one sorted list. 
    Analyze and describe its complexity.

    Example:

    Input:
    [
      1->4->5,
      1->3->4,
      2->6
    ]
    Output: 1->1->2->3->4->4->5->6

    https://leetcode.com/problems/merge-k-sorted-lists/description/
    
    Time : O(N*k), N = total number of elements in all lists
                   k = number of list
    Space: O(N)
    Note :
    '''
    if not lists or len(lists) == 0:
            return []

    clean_empty_elems(lists)
    print(lists)
    merged_arr = merged_arr_head = None
    while True:
        minnode = find_min(lists)
        if minnode == None:
            break
        if merged_arr_head == None:
            merged_arr_head = merged_arr = minnode
        else:
            merged_arr.next = minnode
            merged_arr = merged_arr.next

    if lists and lists[-1]:
        if merged_arr_head == None:
            merged_arr_head = lists[-1]
        else:
            merged_arr.next = lists[-1]
    return merged_arr_head

def make_list(num_arr):
    if num_arr == None:
        raise ValueError(" error")

    head = None
    curr = None
    for x in num_arr:
        if head == None:
            head = curr = ListNode(x)
        else:
            curr.next = ListNode(x)
            curr = curr.next

    return head

def run():

    #list_ln = [make_list([1, 4, 5]), make_list([1, 3, 4]), make_list([2, 6])]
    #print(list_ln)
    #merged_ln = merge_k_sorted_lists(list_ln)
    #print(merged_ln)

    #list_ln = [make_list([2]), make_list([]), make_list([-1])]
    #print(list_ln)
    #merged_ln = merge_k_sorted_lists(list_ln)
    #print(merged_ln)

    #list_ln = [make_list([]), make_list([-1,5,11]), make_list([6,10])]
    #clean_empty_elems(list_ln)
    #print(list_ln)
    #merged_ln = merge_k_sorted_lists(list_ln)
    #print(merged_ln)

    list_ln = [make_list([-1,1]), make_list([-3,1,4]), make_list([-2,-1,0,2])]
    #print(list_ln)
    merged_ln = merge_k_sorted_lists(list_ln)
    print(merged_ln)


if __name__ == '__main__':
    run()

