#!/usr/local/bin/python3

def longest_mountain_in_array(mnt_arr):
    '''
    Let's call any (contiguous) subarray B (of A) a 
    mountain if the following properties hold:

    B.length >= 3
    There exists some 0 < i < B.length - 1 such that 
    B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
    (Note that B could be any subarray of A, 
    including the entire array A.)

    Given an array A of integers, return the length of 
    the longest mountain. 

    Return 0 if there is no mountain.

    Example 1:

    Input: [2,1,4,7,3,2,5]
    Output: 5
    Explanation: The largest mountain is [1,4,7,3,2] which 
    has length 5.
    Example 2:

    Input: [2,2,2]
    Output: 0
    Explanation: There is no mountain.
    Note:

    0 <= A.length <= 10000
    0 <= A[i] <= 10000
    Follow up:

    Can you solve it using only one pass?
    Can you solve it in O(1) space?
    
    https://leetcode.com/problems/longest-mountain-in-array/description/

    Time :
    Space:
    Note :
    a < b > c > d < e < f < g > h > i > j > k
    0   1   2   0   1   2   3   4   5   6   7
    1. current_length, global_length
    2. start from index one, set current and global to 0
    3. if current is less than both left and right 
        then reset current max to zero
    4. otherwise increase both current max
    5. reset global max = max(global max, current max)
    '''
    if mnt_arr == None or len(mnt_arr) < 3:
        return 0

    up, down, tot = 0, 0, 0
    for idx in range(1, len(mnt_arr) - 1):
        if (mnt_arr[idx-1] >= mnt_arr[idx] and 
             mnt_arr[idx] <= mnt_arr[idx+1]):
            up = 0
            down = 0
        else:
            if mnt_arr[idx] > mnt_arr[idx-1]:
                up += 1
            if mnt_arr[idx] > mnt_arr[idx+1]:
                down += 1

        if up > 0 and down > 0:
            tot = max(tot, (up+down)+1)

    return tot

def run():
    print(longest_mountain_in_array([2,1,4,7,3,2,5]))
    print(longest_mountain_in_array([2,2,2]))
    print(longest_mountain_in_array([1,2,3]))
    print(longest_mountain_in_array([3,2,1]))
    print(longest_mountain_in_array([]))
    print(longest_mountain_in_array([3,2,1,3,4,5,6,7,8,8]))
    print(longest_mountain_in_array([1,2,3,4,3,2,1]))
    print(longest_mountain_in_array([2,3,3,2,0,2]))

if __name__ == '__main__':
    run()

