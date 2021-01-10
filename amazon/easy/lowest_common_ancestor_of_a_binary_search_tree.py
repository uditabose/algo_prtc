#!/usr/local/bin/python3

import os
import sys
ds_path = "/Users/papa/spaces/workspace/algo_prtc/basic/ds/"
# ds_path = "/Users/papa/spaces/workspace/AlgoPractice/python/ds/"
sys.path.append(ds_path)

from tree import *


def lowest_common_ancestor_of_a_binary_search_tree(tree, one, two):
    """
    Given a binary search tree (BST), find the lowest
    common ancestor (LCA) of two given nodes in the BST.

    According to the definition of LCA on Wikipedia:
    “The lowest common ancestor is defined between two
    nodes p and q as the lowest node in T that has both
    p and q as descendants (where we allow a node to be a
    descendant of itself).”

    Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]

            _______6______
           /              \
        ___2__          ___8__
       /      \        /      \
       0      _4       7       9
             /  \
             3   5
    Example 1:

    Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
    Output: 6
    Explanation: The LCA of nodes 2 and 8 is 6.
    Example 2:

    Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
    Output: 2
    Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself
                 according to the LCA definition.
    Note:

    All of the nodes' values will be unique.
    p and q are different and both values will exist in the BST.

    https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

    Time : O(N)
    Space: O(N), traversal set
    Note :
    1. keep a path set
    2. pick one and traverse tree to find the path
    3. then traverse for the second and find
        the matching part of the traversed path
    4. last value in the matching path is the LCA
    """
    if not tree:
        return None

    path_set = []
    curr = tree

    # traverse for one
    while curr:
        path_set.append(curr.value)
        if curr.value == one:
            break
        if curr.value > one:
            curr = curr.left
        else:
            curr = curr.right

    # traverse for two
    curr = tree
    lca = None
    print(path_set)
    while curr:
        if curr.value in path_set:
            lca = curr.value

            if curr.value == two:
                break
            if curr.value > two:
                curr = curr.left
            else:
                curr = curr.right
        else:
            break

    return lca


def run():
    '''
    tree = make_binary_tree([6,2,8,0,4,7,9,3,5])
    print(lowest_common_ancestor_of_a_binary_search_tree(tree, 2, 8))
    print()
    tree = make_binary_tree([6,2,8,0,4,7,9,3,5])
    print(lowest_common_ancestor_of_a_binary_search_tree(tree, 2, 4))
    print()
    '''
    tree = make_binary_tree([2,1])
    print(lowest_common_ancestor_of_a_binary_search_tree(tree, 1, 2))
    print()

if __name__ == '__main__':
    run()
