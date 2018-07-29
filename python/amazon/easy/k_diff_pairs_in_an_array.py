#!/usr/local/bin/python3

def add_sorted(pair_set, num1, num2):
    pair_set.add((min(num1, num2), max(num1, num2)))

def k_diff_pairs_in_an_array(num_arr, diff):
    '''
    Given an array of integers and an integer k, you need 
    to find the number of unique k-diff pairs in the array. 
    Here a k-diff pair is defined as an integer pair (i, j), 
    where i and j are both numbers in the array and their 
    absolute difference is k.

    Example 1:
    Input: [3, 1, 4, 1, 5], k = 2
    Output: 2
    Explanation: There are two 2-diff pairs in the array, 
    (1, 3) and (3, 5).
    Although we have two 1s in the input, we should only 
    return the number of unique pairs.
    
    Example 2:
    Input:[1, 2, 3, 4, 5], k = 1
    Output: 4
    Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
    
    Example 3:
    Input: [1, 3, 1, 5, 4], k = 0
    Output: 1
    Explanation: There is one 0-diff pair in the array, (1, 1).
    
    Note:
    The pairs (i, j) and (j, i) count as the same pair.
    The length of the array won't exceed 10,000.
    All the integers in the given input belong to the range: [-1e7, 1e7].
    
    https://leetcode.com/problems/k-diff-pairs-in-an-array/description/

    Time : O(N)
    Space: O(N)
    Note :
    Somewhat 2-sum approach
    1. a set to keep abs(num-2), another set to keep the pairs
    2. if a abs(num-2) is not in set put num in set
    3. if number is there, then put the sorted pair in other set
    4. return the length of second set

    
    '''
    if not num_arr:
        return 0
    if diff < 0:
        # absolute difference can not be negative
        return 0

    diff_set = set()
    pair_set = set()

    for x in num_arr:
        if (x-diff) in diff_set:
            add_sorted(pair_set, x, x-diff)
        if (x+diff) in diff_set:
            add_sorted(pair_set, x, x+diff)

        diff_set.add(x)

    print(pair_set)
    return len(pair_set)

def run():
    '''
    num_arr = [3, 1, 4, 1, 5]
    diff = 2
    print(k_diff_pairs_in_an_array(num_arr, diff))

    num_arr = [1, 2, 3, 4, 5]
    diff = 1
    print(k_diff_pairs_in_an_array(num_arr, diff))

    num_arr = [1, 3, 1, 5, 4]
    diff = 0
    print(k_diff_pairs_in_an_array(num_arr, diff))
    
    num_arr = [1,2,3,4,5]
    diff = -1
    print(k_diff_pairs_in_an_array(num_arr, diff))
    '''

    num_arr = [6,3,5,7,2,3,3,8,2,4]
    diff = 2
    print(k_diff_pairs_in_an_array(num_arr, diff))

if __name__ == '__main__':
    run()

