
def valid_parentheses(paren_str):
    '''

    Given a string containing just the characters 
    '(', ')', '{', '}', '[' and ']', determine if the 
    input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Note that an empty string is also considered valid.

    Example 1:
    Input: "()"
    Output: true
    
    Example 2:
    Input: "()[]{}"
    Output: true
    
    Example 3:
    Input: "(]"
    Output: false
    
    Example 4:
    Input: "([)]"
    Output: false
    
    Example 5:
    Input: "{[]}"
    Output: true
    
    https://leetcode.com/problems/valid-parentheses/description/
    
    Time : O(N)
    Space: O(N)
    Note : 

    1. Create a stack
    2. Put each character
    3. If any of closing brackets : )/}/], then matching starts
    4. Matches to complimentary open bracket : (/{/[; keep going
    5. Does not match return false
    6. If the stack is empty, return true
    '''
    
    if paren_str == None or len(paren_str) == 0:
        return False

    paren_stack = []
    open_paren = '({['
    close_paren = ')}]'
    for bstr in paren_str:
        if bstr in open_paren:
            paren_stack.append(bstr)
        else:
            if len(paren_stack) == 0:
                return False
            
            prev_paren = paren_stack.pop()
            if not (prev_paren in open_paren):
                return False
            elif prev_paren != '(' and bstr == ')':
                return False
            elif prev_paren != '{' and bstr == '}':
                return False
            elif prev_paren != '[' and bstr == ']':
                return False

    return len(paren_stack) == 0

def run():
    paren_str = "()"
    print("%s is valid : %s" % 
          (paren_str, str(valid_parentheses(paren_str))))

    paren_str = "()[]{}"
    print("%s is valid : %s" % 
          (paren_str, str(valid_parentheses(paren_str))))

    paren_str = "(]"
    print("%s is valid : %s" % 
          (paren_str, str(valid_parentheses(paren_str))))

    paren_str = "([)]"
    print("%s is valid : %s" % 
          (paren_str, str(valid_parentheses(paren_str))))

    paren_str = "{[]}"
    print("%s is valid : %s" % 
          (paren_str, str(valid_parentheses(paren_str))))

if __name__ == '__main__':
    run()

