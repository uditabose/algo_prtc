
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
'''
    def lookup_recursive(self, new_value):
        this_node = self.head
        if this_node == None:
            raise ValueError(" invalid tree ")

        if this_node.left == None and this_node.right == None:
            return this_node

        if this_node.value >= new_value and this_node.left == None:
            return this_node
        else:
            return this_node.left.lookup(new_value)

        if this_node.value < new_value and this_node.right == None:
            return this_node
        else:
            return this_node.right.lookup(new_value)
'''

def is_binary_tree(btn):
    if btn == None:
        return True

    if not isinstance(btn, BinaryTreeNode):
        return False

    curr_node = btn
    is_binary = True

    left = curr_node.left
    right = curr_node.right

    print("left : %s" % ("None" if left == None else str(left.value)))
    print("curr_node : %s" % ("None" if curr_node == None else str(curr_node.value)))
    print("right : %s" % ("None" if right == None else str(right.value)))
    
    is_binary = (left == None or left.value < curr_node.value)
    is_binary = (is_binary and (right == None 
                 or right.value >= curr_node.value))

    print("is_binary : %s" % str(is_binary))
    print("----------")

    if is_binary:
        return is_binary_tree(left) and is_binary_tree(right)
    else:
        return is_binary

if __name__ == '__main__':
    array_num = [7346,3342,78,232,676,1218, 24785]
    bst = BinarySearchTree(array_num[0])
    for num in array_num[1:]:
        bst.insert(num)

    print(bst)
    print(is_binary_tree(bst.head))
        
          

        
        
