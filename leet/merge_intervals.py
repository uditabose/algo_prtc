
def merge_intervals(in_arr):
    '''
    Given a collection of intervals, merge all overlapping intervals.

    https://leetcode.com/problems/merge-intervals/description/

    Time : O(N)
    Space: O(N)
    Note : Assume ranges are sorted, if not see cake/merging_ranges.py
    '''
    out_arr = [in_arr[0]]
    for arr in in_arr[1:]:
        mr_arr = out_arr[-1]
        if arr[0] <= mr_arr[1]:
            mr_arr[1] = arr[1]
        else:
            out_arr.append(arr)

    return out_arr
        

def run():
    in_arr = [[1,3],[2,6],[8,10],[15,18]]
    #out_arr = [[1,6],[8,10],[15,18]]
    out_arr = merge_intervals(in_arr)
    print("%s\n%s" % (in_arr, out_arr))

    in_arr = [[1,4],[4,5]]
    #out_arr = [[1,5]]
    out_arr = merge_intervals(in_arr)
    print("%s\n%s" % (in_arr, out_arr))

if __name__ == '__main__':
    run()

