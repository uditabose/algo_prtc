#!/usr/local/bin/python3
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree(TreeNode):
    """ BinarySearchTree """
    def __init__(self, value):
        super(BinarySearchTree, self).__init__(value)
    
    def add_node(self, value):
        curr = self
        prev = None
        while curr:
            if value <= curr.value:
                prev = curr
                curr = curr.left
            else:
                prev = curr
                curr = curr.right

        node = BinarySearchTree(value)
        if value <= prev.value:
            prev.left = node
        else:
            prev.right = node

def make_bst(arr):
    if not arr:
        return None

    bst = BinarySearchTree(arr[0])
    for v in arr[1:]:
        bst.add_node(v)
    return bst

def sum_greater(tree, prev):
    if not tree or not tree.value:
        return 0

    if not tree.right:
        if prev and prev.value > tree.value:
            return prev.value + tree.value
        else:
            return tree.value
    elif prev and prev.value > tree.value:
        return prev.value + sum_greater(tree.right, tree)
    else:
        return sum_greater(tree.right, tree)
    

def convert_bst_to_greater_tree(tree):
    '''
    Given a Binary Search Tree (BST), convert it to a 
    Greater Tree such that every key of the original BST 
    is changed to the original key plus sum of all keys 
    greater than the original key in BST.

    Example:

    Input: The root of a Binary Search Tree like this:
                  5
                /   \
               2     13

    Output: The root of a Greater Tree like this:
                 18
                /   \
              20     13
    
    https://leetcode.com/problems/convert-bst-to-greater-tree/description/

    Time :
    Space:
    Note :
    So there are 2 values need to be taken care of
    1. root of current node
    2. right subtree of the current node

    So, course of action -
    1. tackle right subtree of a node
        a. add that to root 
    2. go to the left, add 

    '''
    
    great_tree = []
    sum_greater(tree, None)
    return great_tree

def run():
    print(convert_bst_to_greater_tree(make_bst([5,3,13,1,4,10,18])))

if __name__ == '__main__':
    run()

