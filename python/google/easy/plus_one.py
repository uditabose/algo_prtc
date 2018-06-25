
def plus_one(num_arr):
    '''
    Given a non-empty array of digits representing a 
    non-negative integer, plus one to the integer.

    The digits are stored such that the most significant 
    digit is at the head of the list, and each element in 
    the array contain a single digit.

    You may assume the integer does not contain any leading zero, 
    except the number 0 itself.

    Example 1:

    Input: [1,2,3]
    Output: [1,2,4]
    Explanation: The array represents the integer 123.
    Example 2:

    Input: [4,3,2,1]
    Output: [4,3,2,2]
    Explanation: The array represents the integer 4321.

    Time : O(N)
    Space: O(1)
    Note :

    1. start from end
    2. add one to the last value, sum = (val + 1) % 10
    3. compute carry, carry = int((val + 1) / 10)
    4. add carry to previous elem
    5. return resultant array
    '''
    if num_arr == None or len(num_arr) == 0:
        return num_arr

    add_val = 1
    summ = 0
    carry = 0
    for idx in range(len(num_arr) - 1, -1, -1):
        val = num_arr[idx]
        summ = (val + add_val + carry) % 10
        carry = int((val + add_val + carry) / 10)

        num_arr[idx] = summ
        add_val = 0

    if carry > 0:
        num_arr.insert(0, carry)

    return num_arr

def run():
    num_arr = [1,2,3]
    print("one plus %s" % plus_one(num_arr))

    num_arr = [4,3,2,1]
    print("one plus %s" % plus_one(num_arr))

    num_arr = [9]
    print("one plus %s" % plus_one(num_arr))

    num_arr = [9,9,9,9]
    print("one plus %s" % plus_one(num_arr))

if __name__ == '__main__':
    run()

