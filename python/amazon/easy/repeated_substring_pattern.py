#!/usr/local/bin/python3

def verify_sub(astr, sub):
    print(sub)
    if not sub:
        return False

    length = len(sub)
    if len(astr) % length != 0:
        return False

    othstr = sub * (int(len(astr) / length))
    return othstr == astr

def repeated_substring_pattern(astr):
    '''
    Given a non-empty string check if it can be constructed 
    by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.
    
    Example 1:
    Input: "abab"

    Output: True

    Explanation: It's the substring "ab" twice.
    Example 2:
    Input: "aba"

    Output: False
    Example 3:
    Input: "abcabcabcabc"

    Output: True

    Explanation: It's the substring "abc" four times. 
    (And the substring "abcabc" twice.)
    
    https://leetcode.com/problems/repeated-substring-pattern/description/

    Time : O(N)
    Space: O(1)
    Note :
    1. two counters, one at zero, another at one
    2. first counter is used to find max length of possible substring
    3. at first, 
        a. match the strings 0-start,  start+1-last
        b. if equal, found the substring
        c. if not, update start = start+1
        d. if start > length/2, then return false
        e. else repeat from step 3a.
    4. if we have a substring, then match in group
        a. if the entire string matches, then return true
        b. if not, return false

    '''
    if not astr:
        return False

    length = 1
    sub = None
    while length <= len(astr)/2:
        print("%s:%s" % (astr[0:length], astr[length:2*length]))
        if astr[0:length] == astr[length:2*length]:
            sub = astr[0:length] 
            if verify_sub(astr, sub):
                return True   
        
        length += 1

    return verify_sub(astr, sub)
    

def run():
    astr = "ababababab"
    #'abab'
    print("%s is repeated : %s" 
          % (astr, str(repeated_substring_pattern(astr) )))
    
    astr = 'aba'
    print("%s is repeated : %s" 
          % (astr, str(repeated_substring_pattern(astr) )))
    
    astr = 'abcabcabcabc'
    print("%s is repeated : %s" 
          % (astr, str(repeated_substring_pattern(astr) )))
    
    astr = 'abcabcabcabcab'
    print("%s is repeated : %s" 
          % (astr, str(repeated_substring_pattern(astr) )))
    
    astr = 'abcabcdfabcabc'
    print("%s is repeated : %s" 
          % (astr, str(repeated_substring_pattern(astr) )))
    
    
if __name__ == '__main__':
    run()

