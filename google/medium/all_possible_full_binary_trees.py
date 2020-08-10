#!/usr/local/bin/python3


def all_possible_full_binary_trees(no_of_elems):
  """
    https://leetcode.com/problems/all-possible-full-binary-trees

    A full binary tree is a binary tree where each node has exactly 0 or 2 children.
    Return a list of all possible full binary trees with N nodes.
    Each element of the answer is the root node of one possible tree.
    Each node of each tree in the answer must have node.val = 0.
    You may return the final list of trees in any order.

    Example 1:

    Input: 7
    Output: [
    [0,0,0,null,null,0,0,null,null,0,0],
    [0,0,0,null,null,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,null,null,null,null,0,0],
    [0,0,0,0,0,null,null,0,0]]

    Time :
    Space:
    Note :
    Similar to all enclosing parenthesis problem

    pre-condition:
        n => number of elements

    1. create a list => mother_list
    2. initialize
        2a. mother_list << [0]
        2b. count = 0
        2c. not_converged = true
    3. loop true
        temp_mother_list = []
        4. mother_list.pop => sub_list
        5. if len(sub_list) < n
            6. loop sub_list
                7. create temp_list => pad (null 0 null)
                8. temp_mother_list << temp_list
    """
  if no_of_elems == 0:
    return []
  if no_of_elems % 2 == 0:
    return None

  mother_list = [[0]]

  while True:
    temp_mother_list = []
    while len(mother_list) > 0:
      sub_list = mother_list.pop()
      if len(sub_list) < no_of_elems:
        temp_sub_list = []
        for e in sub_list:
          if e == 0:
            temp_sub_list.extend([0, 1, 0])
          else:
            temp_sub_list.append(1)


def run():
  pass


if __name__ == '__main__':
  run()
