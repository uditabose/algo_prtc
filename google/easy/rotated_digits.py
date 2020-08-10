
'''

num = 10a + b
dig = map[b]

rest = 10a

fnum = 10a + dig

'''

def rotate_num(num):
    rotate_map = {0:0, 1:1, 2:5, 3:None, 4:None, 5:2, 6:9, 7:None, 8:8, 9:6}
    if num < 10:
        return rotate_map[num]
    
    rot_num = ""
    while num > 0:
        #print("rot_num %s :: num %d " % (rot_num, num))
        dig = rotate_map[num % 10]

        num = int(num / 10)
        if dig == None:
            return None
        else:
            rot_num = str(dig) +  rot_num 
  
    return int(rot_num)
        
def rotated_digits(num):
    '''
    X is a good number if after rotating each digit 
    individually by 180 degrees, we get a valid number 
    that is different from X.  Each digit must be rotated
     - we cannot choose to leave it alone.

    A number is valid if each digit remains a digit after 
    rotation. 0, 1, and 8 rotate to themselves; 2 and 5 
    rotate to each other; 6 and 9 rotate to each other, 
    and the rest of the numbers do not rotate to any other 
    number and become invalid.

    Now given a positive number N, how many numbers X 
    from 1 to N are good?

    Example:
    Input: 10
    Output: 4
    Explanation: 
    There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
    Note that 1 and 10 are not good numbers, 
    since they remain unchanged after rotating.
    Note:

    N  will be in range [1, 10000].

    https://leetcode.com/problems/rotated-digits/description/
    Time :
    Space:
    Note :
    '''
    num_rotated = set()
    for x in range(1, num+1):
        rot_num = rotate_num(x)

        if rot_num != None and rot_num != x:
            #print("x = %d   rot = %d" % (x, rot_num))
            num_rotated.add(rot_num)

    #print(num_rotated)
    return len(num_rotated)

def run():

    print("%d" % rotated_digits(1))
    print("%d" % rotated_digits(2))
    print("%d" % rotated_digits(3))
    print("%d" % rotated_digits(4))
    print("%d" % rotated_digits(10))
    print("%d" % rotated_digits(20))
    print("%d" % rotated_digits(278))

    '''
    0
    1
    1
    1
    4
    7
    115

    0
    1
    1
    1
    5
    8
    105
    '''

if __name__ == '__main__':
    run()

