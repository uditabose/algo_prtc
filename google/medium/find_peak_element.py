#!/usr/local/bin/python3

def find_peak_element(peak_arr):
    '''
    
    A peak element is an element that is greater than its neighbors.
    Given an input array nums, where nums[i] ≠ nums[i+1], 
    find a peak element and return its index.
    The array may contain multiple peaks, in that case 
    return the index to any one of the peaks is fine.

    You may imagine that nums[-1] = nums[n] = -∞.

    Example 1:

    Input: nums = [1,2,3,1]
    Output: 2
    Explanation: 3 is a peak element and your function should return the index number 2.
    Example 2:

    Input: nums = [1,2,1,3,5,6,4]
    Output: 1 or 5 
    Explanation: Your function can return either index number 1 where the peak element is 2, 
                 or index number 5 where the peak element is 6.
    Note:

    Your solution should be in logarithmic complexity.
    
    https://leetcode.com/problems/find-peak-element/description

    Time :
    Space:
    Note :
    This is a strange problem statement, and requirement. Without any more information this seems a straight 
    O(N) kind of solution. Logarithmic solution needs some form of sorting involved, but the input array is 
    unsorted and without sorting this kind of odd.
    
    One dang idea : 
    1. choose any index
    2. if idx-1 < idx > idx+1, return idx
    3. if idx-1 < idx < idx+1, choose idx+1, repeat step 2
    4. if idx-1 > idx > idx+1, choose idx-1, repeat step 2
    
    So the idea is we will only pick the value larger than partition index value, 
    in that case at every step halving the options
    '''
    if peak_arr == None or len(peak_arr) == 1:
        return 0
    elif len(peak_arr) == 2:
        if peak_arr[0] > peak_arr[1]:
            return 0
        else:
            return 1

    part =  int((len(peak_arr) - 0)/2)
    print(part)
    
    while part - 1 >= 0 and part + 1 < len(peak_arr):
        if (peak_arr[part - 1] < peak_arr[part] 
            and peak_arr[part + 1] < peak_arr[part]):
            return part
        elif (peak_arr[part - 1] > peak_arr[part] 
              and peak_arr[part + 1] < peak_arr[part]):
            part = part - 1
        else:
            part = part + 1
                
    return -1
            
def run():
    print(find_peak_element([1,2,1]))
    #print(find_peak_element([1,2,3,1]))
    #print(find_peak_element([1,2,1,3,5,6,4]))

if __name__ == '__main__':
    run()

