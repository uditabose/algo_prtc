
def strobogrammatic_number(num_str):
    '''
    
    A strobogrammatic number is a number that looks the 
    same when rotated 180 degrees (looked at upside down).

    Write a function to determine if a number is 
    strobogrammatic. The number is represented as a string.

    Example 1:
    Input:  "69"
    Output: true
    
    Example 2:
    Input:  "88"
    Output: true

    Example 3:
    Input:  "962"
    Output: false

    https://leetcode.com/problems/strobogrammatic-number/description/

    Time : O(N)
    Space: O(1)
    Note :
    1. 2 indices, left-end and right-end
    2. if characters match, both must be in `018` to go on
    3. if they don't, but both in `69`, that's cool too
    4. or else false
    '''
    sub_grp_1 = '018'
    sub_grp_2 = '69'

    if len(num_str) < 2:
        return num_str in sub_grp_1
    i = 0
    j = len(num_str) - 1

    while i < j:
        left = num_str[i]
        right = num_str[j]

        i += 1
        j -= 1

        if left == right and left in sub_grp_1:
            continue
        elif left != right and left in sub_grp_2 and right in sub_grp_2:
            continue
        else:
            return False

    if i == j:
        return num_str[i] in sub_grp_1
    return True

def run():
    num_str = "69"
    print("strobogrammatic %s" % str(strobogrammatic_number(num_str)))

    num_str = "88"
    print("strobogrammatic %s" % str(strobogrammatic_number(num_str)))

    num_str = "692"
    print("strobogrammatic %s" % str(strobogrammatic_number(num_str)))

    num_str = "018"
    print("strobogrammatic %s" % str(strobogrammatic_number(num_str)))

if __name__ == '__main__':
    run()

