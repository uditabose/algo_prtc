#!/usr/local/bin/python3

class Node(object):
    """ a tree node """
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def get_children(tree_rep, rep_str, tree_node):
    if tree_node == None:
        return 

    last = ("%s->" % rep_str) if len(rep_str) > 0 else ""
    last = "%s%s" % (last, tree_node.val)
    
    if tree_node.left == None and tree_node.right == None:
        # if have reached a leaf node, then add that string
        tree_rep.append(last)
        # otherwise keep on adding left and then right
    if tree_node.left != None:
        get_children(tree_rep, last, tree_node.left)
    if tree_node.right != None:
        get_children(tree_rep, last, tree_node.right)
      
def binary_tree_paths(tree_root):
    '''

    Given a binary tree, return all root-to-leaf paths.
    Note: A leaf is a node with no children.
    
    Example:
    Input:

       1
     /   \
    2     3
     \
      5

    Output: ["1->2->5", "1->3"]

    Explanation: All root-to-leaf paths are: 1->2->5, 1->3
    
    https://leetcode.com/problems/binary-tree-paths/description/

    Time :
    Space:
    Note :
    '''

    if tree_root == None:
        return []
    if tree_root.val == None:
        return []

    tree_rep = []
    get_children(tree_rep, "", tree_root)  
    return tree_rep

def run():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(5)

    print(binary_tree_paths(root))

if __name__ == '__main__':
    run()

