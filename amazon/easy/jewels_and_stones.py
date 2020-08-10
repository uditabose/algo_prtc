#!/usr/local/bin/python3

def is_empty(iter_type):
    return iter_type == None or len(iter_type) == 0

def jewels_and_stones(jewel, stone):
    '''
    You're given strings J representing the types 
    of stones that are jewels, and S representing the 
    stones you have.  Each character in S is a type of 
    stone you have.  You want to know how many of the 
    stones you have are also jewels.

    The letters in J are guaranteed distinct, and all 
    characters in J and S are letters. Letters are case 
    sensitive, so "a" is considered a different type of stone from "A".

    Example 1:

    Input: J = "aA", S = "aAAbbbb"
    Output: 3
    Example 2:

    Input: J = "z", S = "ZZ"
    Output: 0

    https://leetcode.com/problems/jewels-and-stones/description/

    Time : O(n), n = length of stone string
    Space: O(k), k = length of jewel string
    Note :
    1. create a set from jewel string, initialize jewel count to zero
    2. loop through the stones string
    3. if stone char in jewel set, increment jewel count
    4. return jewel count
    '''
    if is_empty(jewel) or is_empty(stone):
        return 0

    jewel_set = set(jewel)
    jcnt = 0
    for char in stone:
        if char in jewel_set:
            jcnt += 1

    return jcnt
        
def run():
    print(jewels_and_stones('aA', 'aAAbbbb'))
    print(jewels_and_stones('z', 'ZZ'))

if __name__ == '__main__':
    run()

