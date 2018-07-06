#!/usr/local/bin/python3

def h_index(citations):
    '''
    Given an array of citations (each citation is a non-negative 
    integer) of a researcher, write a function to compute 
    the researcher's h-index.

    According to the definition of h-index on Wikipedia: 
    "A scientist has index h if h of his/her N papers 
    have at least h citations each, and the other N − h 
    papers have no more than h citations each."

    Example:

    Input: citations = [3,0,6,1,5]
    Output: 3 
    Explanation: [3,0,6,1,5] means the researcher has 
                 5 papers in total and each of them had 
                 received 3, 0, 6, 1, 5 citations respectively. 
                 Since the researcher has 3 papers with at least 3
                  citations each and the remaining 
                 two with no more than 3 citations each, 
                 her h-index is 3.
    Note: If there are several possible values for h, 
    the maximum one is taken as the h-index.
    
    https://leetcode.com/problems/h-index/description/

    Time : O(NlogN)
    Space: 
    Note :
    1. sort, reverse
    2. mid index >= array[mid index]
    
    '''
    if citations == None or len(citations) == 0:
        return 0
    #if len(citations) == 1:
        #return 1

    sorted_cit = sorted(citations)
    len_cit = len(citations)
    h_index = None
    for idx in range(0, len_cit):
        if len_cit - idx >= sorted_cit[idx]:
            h_index = sorted_cit[idx]

    return h_index if h_index != None else 1
    
def run():
    print("h-index : %d" % h_index([3,0,6,1,5]))
    print("h-index : %d" % h_index([]))
    print("h-index : %d" % h_index([1]))
    print("h-index : %d" % h_index([2]))
    print("h-index : %d" % h_index([1,2]))
    print("h-index : %d" % h_index([0,2]))
    print("h-index : %d" % h_index([10,20]))

if __name__ == '__main__':
    run()

