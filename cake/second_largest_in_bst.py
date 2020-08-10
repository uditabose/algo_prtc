
class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

    def __repr__(self):
        tree_rep = " (%s) " % str(self.value)
        left_repr = ""
        right_repr = ""
        
        if self.left != None:
            left_repr = "%s <- " % str(self.left)

        tree_rep = " %s " % str(self.value)

        if self.right != None:
            right_repr = " -> %s" % str(self.right)

        return "%s%s%s" % (left_repr, tree_rep, right_repr)

class BinarySearchTree():
    """
    https://www.interviewcake.com/question/python/bst-checker

    Write a function to check that a binary tree 
    is a valid binary search tree. 
    """
    def __init__(self, value):
        self.head = BinaryTreeNode(value)

    def insert(self, new_value):
        curr_parent = self.lookup(new_value)
        if curr_parent == None:
            raise IndexError(" bad insert ")
        
        if curr_parent.value >= new_value:
            curr_parent.insert_left(new_value)
        else:
            curr_parent.insert_right(new_value)
    
    def __repr__(self):
        return str(self.head)

    def lookup(self, new_value):
        this_node = self.head
        if this_node == None:
            raise ValueError(" invalid tree ")

        while True:

            # this is a leaf node
            if this_node.left == None and this_node.right == None:
                break

            # go left
            if this_node.value >= new_value :
                if this_node.left == None:
                    break
                else:
                    this_node = this_node.left

            # go right
            if this_node.value < new_value :
                if this_node.right == None:
                    break
                else:
                    this_node = this_node.right

        return this_node

def create_bst(num_arr):
    if num_arr == None or len(num_arr) == 0:
        raise ValueError(" not a valid number array ")

    bst = BinarySearchTree(num_arr[0])
    for num in num_arr[1:]:
        bst.insert(num)

    return bst

def find_2nd_last_right(btn):
    if btn == None:
        return None

    curr_node = btn
    prev_node = None
    while curr_node.right != None:
        prev_node = curr_node
        curr_node = curr_node.right

    return prev_node

def find_2nd_last(btn):
    if btn == None:
        return None

    curr_node = btn
    prev_node = curr_node.left if curr_node.right == None else None

    while curr_node != None:
        if curr_node.right != None:
            prev_node = curr_node
            curr_node = curr_node.right
        else:
            curr_node = curr_node.left

    return prev_node
        

def second_largest_in_bst(bst):
    '''
    Write a function to find the 2nd 
    largest element in a binary search tree. 
    
    https://www.interviewcake.com/question/python/second-largest-item-in-bst
    '''
    if bst == None or bst.head == None:
        return None

    tgt_node = None
    tgt_node = find_2nd_last(bst.head)
    '''
    if bst.head.right == None:
        #tgt_node = find_2nd_last_left(bst.head)
        tgt_node = find_2nd_last(bst.head.left)
    else:
        #tgt_node = find_2nd_last_right(bst.head)
        tgt_node = find_2nd_last(bst.head.right)
    '''
    return tgt_node
        

if __name__ == "__main__":
    bst = create_bst([7346,3342,78,232,676,1218, 24785])
    sec_last = second_largest_in_bst(bst)
    print("second last : %s" % ("None" if sec_last == None else str(sec_last.value)))

    bst = create_bst([10, 20, 30, 40, 50, 60, 70])
    sec_last = second_largest_in_bst(bst)
    print("second last : %s" % ("None" if sec_last == None else str(sec_last.value)))

    bst = create_bst([70, 60, 50, 40, 30, 20, 10])
    sec_last = second_largest_in_bst(bst)
    print("second last : %s" % ("None" if sec_last == None else str(sec_last.value)))

    bst = create_bst([100, 110, 90, 80, 70, 120, 130])
    sec_last = second_largest_in_bst(bst)
    print("second last : %s" % ("None" if sec_last == None else str(sec_last.value)))






