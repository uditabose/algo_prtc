#!/usr/local/bin/python3
class Node(object):
    """docstring for Node"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def merge_tree(root, tree1, tree2):
  if root:
    pass

def merge_two_binary_trees(tree1, tree2):
    '''
    Given two binary trees and imagine that when you put one 
    of them to cover the other, some nodes of the two trees 
    are overlapped while the others are not.

    You need to merge them into a new binary tree. 
    The merge rule is that if two nodes overlap, then 
    sum node values up as the new value of the merged node. 
    Otherwise, the NOT null node will be used as the node of new tree.

    Example 1:
    Input: 
        Tree 1                     Tree 2                  
              1                         2                             
             / \                       / \                            
            3   2                     1   3                        
           /                           \   \                      
          5                             4   7                  
    Output: 
    Merged tree:
             3
            / \
           4   5
          / \   \
         5   4   7
    Note: The merging process must start from the root nodes of both trees.
    
    https://leetcode.com/problems/merge-two-binary-trees/description/

    Time :
    Space:
    Note :
    1. 
    '''
    if tree1 == None and tree2 == None:
      return None
    if tree1 == None and tree2 != None:
      return tree2
    if tree1 != None and tree2 == None:
      return tree1

    mroot = Node(tree1.value + tree2.value)
    merge_tree(mroot, tree1, tree2)
    return mroot

    

def run():
    pass

if __name__ == '__main__':
    run()

