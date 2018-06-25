
def find_mnt_index(mnt_arr, first_idx, last_idx):
    if last_idx < first_idx:
        return -1

    if first_idx + 1 == last_idx:
        return last_idx

    mid_idx = first_idx + int((last_idx - first_idx + 1)/2)
    
    print("start %d mid %d last %d" % (first_idx, mid_idx, last_idx))
    
    if (mnt_arr[mid_idx] > mnt_arr[mid_idx - 1] 
        and mnt_arr[mid_idx] > mnt_arr[mid_idx + 1]):
        return mid_idx
    elif (mnt_arr[mid_idx] > mnt_arr[mid_idx - 1] 
          and mnt_arr[mid_idx] < mnt_arr[mid_idx + 1]):
        return find_mnt_index(mnt_arr, mid_idx, last_idx)
    else:
        return find_mnt_index(mnt_arr, first_idx, mid_idx)
    
    

def peak_index_in_a_mountain_array(mnt_arr):
    '''
    Let's call an array A a mountain if the following properties hold:

    A.length >= 3
    There exists some 0 < i < A.length - 1 such 
    that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
    Given an array that is definitely a mountain, 
    return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

    Example 1:

    Input: [0,1,0]
    Output: 1
    Example 2:

    Input: [0,2,1,0]
    Output: 1
    Note:

    3 <= A.length <= 10000
    0 <= A[i] <= 10^6
    A is a mountain, as defined above.

    https://leetcode.com/problems/peak-index-in-a-mountain-array/description/

    Time : O(NlogN)
    Space: O(1)
    Note :

    Consider a[i] : increasing, b[i] : decreasing
    1. find mid value, list[mid]
    2. compare list[mid - 1], list[mid], list[mid + 1]
    3. if list[mid - 1] < list[mid] and list[mid] > list[mid + 1]
        return mid
    4. if list[mid - 1] < list[mid] and list[mid] > list[mid + 1]
        move to left of the list
    5. if list[mid - 1] > list[mid] and list[mid] < list[mid + 1]
        move to right of the list
    '''

    if mnt_arr == None or len(mnt_arr) == 0:
        return -1

    mnt_index = find_mnt_index(mnt_arr, 0, len(mnt_arr) - 1)
    return mnt_index
    

def run():
    #mnt_arr = [0,1,0]
    #print("peak at %d" % peak_index_in_a_mountain_array(mnt_arr))

    #mnt_arr = [0,2,1,0]
    #print("peak at %d" % peak_index_in_a_mountain_array(mnt_arr))

    mnt_arr = [40,48,61,75,100,99,98,39,30,10]
    print("peak at %d" % peak_index_in_a_mountain_array(mnt_arr))


if __name__ == '__main__':
    run()

