
def find_anagram_mappings(a_arr, b_arr):
    '''
    Given two lists A and B, and B is an anagram of A. 
    B is an anagram of A means B is made by randomizing 
    the order of the elements in A.

    We want to find an index mapping P, from A to B. 
    A mapping P[i] = j means the ith element in A appears 
    in B at index j.

    These lists A and B may contain duplicates. 
    If there are multiple answers, output any of them.

    For example, given

    A = [12, 28, 46, 32, 50]
    B = [50, 12, 32, 46, 28]
    
    We should return
    [1, 4, 3, 2, 0]
    as P[0] = 1 because the 0th element of A appears at
     B[1], and P[1] = 4 because the 1st element of 
     A appears at B[4], and so on.
    
    Note:
    A, B have equal lengths in range [1, 100].
    A[i], B[i] are integers in range [0, 10^5].

    https://leetcode.com/problems/find-anagram-mappings/
    
    Time : O(N)
    Space: O(N)
    Note :

    1. Create a map, key : B[i] value, value : [i,...]
    2. Loop over A, put i in position array
    '''

    
    if a_arr == None or b_arr == None:
        return None

    if len(a_arr) != len(b_arr):
        return None

    if len(a_arr) == 0:
        return []

    b_map = {}
    for idx, elem in enumerate(b_arr):
        if elem in b_map:
            b_map[elem].append(idx)
        else:
            b_map[elem] = [idx]

    pos_arr = []
    for elem in a_arr:
        if len(b_map[elem]) > 0:
            pos_arr.append(b_map[elem].pop())

    return pos_arr

def run():
    a_arr = [12, 28, 46, 32, 50]
    b_arr = [50, 12, 32, 46, 28]
    print(find_anagram_mappings(a_arr, b_arr))

    # [1, 4, 3, 2, 0]
    # [1, 4, 3, 2, 0]

if __name__ == '__main__':
    run()

