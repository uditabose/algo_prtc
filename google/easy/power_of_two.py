#!/usr/local/bin/python3

def power_of_two(anum):
    '''
    Given an integer, write a function to determine 
    if it is a power of two.

    Example 1:

    Input: 1
    Output: true 
    Explanation: 20 = 1
    Example 2:

    Input: 16
    Output: true
    Explanation: 24 = 16
    Example 3:

    Input: 218
    Output: false

    https://leetcode.com/problems/power-of-two/description/

    Time :
    Space:
    Note :
    1. keep on halving
    '''

    if anum == 0:
        return False
    elif anum == 1:
        return True

    half = anum

    while half % 2 == 0:
        half = int(half / 2)

    return True if half == 1 else False

def run():
    print("power-of-two : %s" % power_of_two(1))
    print("power-of-two : %s" % power_of_two(16))
    print("power-of-two : %s" % power_of_two(218))

if __name__ == '__main__':
    run()

