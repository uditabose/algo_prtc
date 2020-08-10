
def missing_ranges(nums, lower, upper):
    '''
    Given a sorted integer array nums, where the range 
    of elements are in the inclusive range [lower, upper], 
    return its missing ranges.

    Example:

    Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
    Output: ["2", "4->49", "51->74", "76->99"]
    https://leetcode.com/problems/missing-ranges/description/

    Time :
    Space:
    Note :
    1. keep  previous value
    2. if previous value + 1 < current value,
        missing (previous value + 1 -> current value - 1)
    '''
    if nums == None or len(nums) == 0:
        if lower == upper:
            return ["%d" % lower]
        else:
            return ["%d->%d" % (lower, upper)]
    elif len(nums) == 1:
        if lower == nums[0]:
            if lower + 1 == upper:
                return ["%d" % upper]
            else:
                return ["%d->%d" % (lower+1, upper)]           
        elif upper == nums[0]:
            if lower + 1 == upper:
                return ["%d" % lower]
            else:
                return ["%d->%d" % (lower, upper-1)]
        else:
            ret_arr = []
            diff = nums[0] - lower
            if diff == 1:
                ret_arr.append("%d" % lower)
            else:
                ret_arr.append("%d->%d" % (lower, nums[0]-1))

            diff = upper - nums[0]
            if diff == 1:
                ret_arr.append("%d" % upper)
            else:
                ret_arr.append("%d->%d" % (nums[0]+1, upper))


        
    

    prev_value = nums[0]
    ret_arr = []
    for curr_value in nums:
        if curr_value > upper:
            break

        if curr_value == prev_value + 2:
            ret_arr.append(str(prev_value + 1))
        elif curr_value > prev_value + 2:
            ret_arr.append("%d->%d" % (prev_value + 1, curr_value - 1))
                
        prev_value = curr_value

    print(prev_value)
    if prev_value + 2 == upper:
        ret_arr.append(str(prev_value + 1))
    elif prev_value + 2 < upper:
        ret_arr.append("%d->%d" % (prev_value + 1, upper))

    return ret_arr

def run():
    print(missing_ranges([0, 1, 3, 50, 75], 0, 99))
    print(missing_ranges([-1], -2, -1))

if __name__ == '__main__':
    run()

