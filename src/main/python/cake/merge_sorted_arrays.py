
def merge_sorted_arrays(m_arr, n_arr):
    '''
    In order to win the prize for most cookies sold, my friend Alice 
    and I are going to merge our Girl Scout Cookies orders and enter as one unit.

    Each order is represented by an "order id" (an integer).

    We have our lists of orders sorted numerically already, 
    in lists. Write a function to merge our lists of orders into one sorted list.

    https://www.interviewcake.com/question/python/merge-sorted-arrays?section=array-and-string-manipulation&course=fc1
    
    Time: O(N+M)
    Space: O(N+M)
    Note:
    '''

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

    return merged_arr

if __name__ == '__main__':
    m_arr = [3, 4, 6, 10, 11, 15]
    n_arr = [1, 5, 8, 12, 14, 19]

    print("%s ++ %s" % (m_arr, n_arr))
    print(merge_sorted_arrays(m_arr, n_arr))