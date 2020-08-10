
def longest_valid_parentheses(paren_str):
    '''
    Given a string containing just the characters 
    '(' and ')', find the length of the longest 
    valid (well-formed) parentheses substring.

    https://leetcode.com/problems/longest-valid-parentheses/description/

    Time : O(N)
    Space: O(N)
    Note :
    '''
    
    if paren_str == None or len(paren_str) < 2:
        return ""

    paren_arr = []
    left = len(paren_str) 
    right = 0
    count = 0
    for count, char in enumerate(paren_str):
        if char == ')':            
            if len(paren_arr) > 0:
                lc = paren_arr.pop()
                if lc[0] == '(':
                    right = count
                    left = min(left, lc[1])
        else:
            paren_arr.append((char, count))

    #print(paren_arr)
    if left >= 0 and right < len(paren_str):
        return max(0, (right + 1 - left)), paren_str[left:right+1]
    else:
        return 0, ""

def run():
    paren_str = '(()'
    print(longest_valid_parentheses(paren_str))

    paren_str = ')()())'
    print(longest_valid_parentheses(paren_str))

    paren_str = '(()())'
    print(longest_valid_parentheses(paren_str))

    paren_str = '((()))'
    print(longest_valid_parentheses(paren_str))

    paren_str = '()((()'
    print(longest_valid_parentheses(paren_str))

if __name__ == '__main__':
    run()

