
def median_of_two_sorted_arrays(nums1, nums2):
    '''
    There are two sorted arrays nums1 and nums2 
    of size m and n respectively.

    Find the median of the two sorted arrays. 
    The overall run time complexity should be O(log (m+n)).
    https://leetcode.com/problems/median-of-two-sorted-arrays/description/
    
    Time:
    Space:
    Note:
    '''

    if nums1 == None or nums2 == None:
        return None

    m_arr = nums1
    n_arr = nums2

    merged_arr = []
    m_idx = 0
    n_idx = 0

    while m_idx < len(m_arr) and n_idx < len(n_arr):
        if m_arr[m_idx] <= n_arr[n_idx]:
            merged_arr.append(m_arr[m_idx])
            m_idx += 1
        else:
            merged_arr.append(n_arr[n_idx])
            n_idx += 1

    while m_idx < len(m_arr):
        merged_arr.append(m_arr[m_idx])
        m_idx += 1

    while n_idx < len(n_arr):
        merged_arr.append(n_arr[n_idx])
        n_idx += 1

    #print(merged_arr)
    tot_len = len(merged_arr)
    median_pos = int((tot_len+1)/2)
    #print(median_pos)
    if tot_len % 2 == 0:
        #print((merged_arr[median_pos] 
                      #+ merged_arr[median_pos-1]))
        return (merged_arr[median_pos] 
                      + merged_arr[median_pos-1])/2
    else:
        return merged_arr[median_pos-1]

if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2]
    print("median is %f " % 
          (median_of_two_sorted_arrays(nums1, nums2)))
    
    nums1 = [1, 2]
    nums2 = [3, 4]

    print("median is %f " % 
          (median_of_two_sorted_arrays(nums1, nums2)))
    

