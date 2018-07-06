#!/usr/local/bin/python3

def summary_ranges(in_range):
    '''
    Given a sorted integer array without duplicates, 
    return the summary of its ranges.

    Example 1:

    Input:  [0,1,2,4,5,7]
    Output: ["0->2","4->5","7"]
    Explanation: 0,1,2 form a continuous range; 
    4,5 form a continuous range.
    
    Example 2:

    Input:  [0,2,3,4,6,8,9]
    Output: ["0","2->4","6","8->9"]
    Explanation: 2,3,4 form a continuous range; 
    8,9 form a continuous range.

    https://leetcode.com/problems/summary-ranges/description/

    Time : O(N)
    Space: O(N)
    Note :
    1. start index, end index, curr index
    2. progress, if curr != end + 1:
                        if start == end => "start"
                        else => "start->end"
    3. else: end = curr
    '''
    
    if in_range == None or len(in_range) < 2:
        return [str(in_range[0])]

    start, end = 0, 0
    range_arr = []
    for curr in range(1, len(in_range)):
        if in_range[curr] != in_range[end] + 1:
            if start != end:
                range_arr.append("%d->%d" % (in_range[start], in_range[end])) 
            else:
                range_arr.append("%d" % in_range[start])
            start, end = curr, curr
        else:
            end = curr

    if start != end:
        range_arr.append("%d->%d" % (in_range[start], in_range[end])) 
    else:
        range_arr.append("%d" % in_range[start])

    return range_arr
            
def run():
    in_range = [0,1,2,4,5,7]
    print(summary_ranges(in_range))

    in_range = [0,2,3,4,6,8,9]
    print(summary_ranges(in_range))

    '''
    ["0->2","4->5","7"]
    ['0->2', '4->5', '7']

    ["0","2->4","6","8->9"]
    ['0', '2->4', '6', '8->9']
    '''

if __name__ == '__main__':
    run()

