#!/usr/local/bin/python3

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def attach_node(node, val):
    if val == None:
        return
    new_node = TreeNode(val = val)
    curr_node = node
    prev_node = node
    while curr_node is not None:
        prev_node = curr_node
        if curr_node.val >= val:
            curr_node = curr_node.left
        else:
            curr_node = curr_node.right

    if prev_node.val >= val:
        prev_node.left = new_node
    else:
        prev_node.right = new_node

def make_tree(arr):
    root = TreeNode(val = arr[0])
    for i in arr:
        attach_node(root, i)
    return root

def found_target_sum(node1, node2, target):
    if node1 == None or node2 == None:
        return False

    if node1.val == None or node2.val == None:
        return False

    summed = node1.val + node2.val
    if summed == target:
        return True
    elif summed > target:
        return found_target_sum(node1, node2.left, target) or found_target_sum(node2, node2.left, target)
    else:
        return found_target_sum(node1, node2.right, target) or found_target_sum(node2, node2.right, target)

def two_sum_iv_input_is_a_bst(root, k):
    """
    https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

    Time :
    Space:
    Note :
    """
    if root == None:
        return

    curr_node = root
    return found_target_sum(curr_node,  curr_node.left, k) or found_target_sum(curr_node,  curr_node.right, k)


def run():
    # tree_arr = [5,3,6,2,4,None,7]
    # tree = make_tree(tree_arr)
    # target = 9
    # print(two_sum_iv_input_is_a_bst(tree, target))
    #
    # target = 28
    # print(two_sum_iv_input_is_a_bst(tree, target))

    tree_arr = [2,1,3]
    tree = make_tree(tree_arr)
    target = 4
    print(two_sum_iv_input_is_a_bst(tree, target))


if __name__ == '__main__':
    run()
