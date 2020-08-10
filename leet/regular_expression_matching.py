
class Solution(object):
    def isMatch(self, text, pattern):
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])

def regular_expression_matching(mtc_str, reg_ex):
    '''
    Given an input string (s) and a pattern (p), 
    implement regular expression matching with support for '.' and '*'.

    '.' Matches any single character.
    '*' Matches zero or more of the preceding element.
    The matching should cover the entire input string (not partial).

    Note:

    s could be empty and contains only lowercase letters a-z.
    p could be empty and contains only lowercase letters a-z, 
        and characters like . or *.

    https://leetcode.com/problems/regular-expression-matching/solution/

    Time: 
    Space:
    Note : See solution
    '''

    mtc = "".join(reversed(mtc_str))
    regpos = 0
    mtcchr = 
    reg = "".join(reversed(reg_ex))
    regchr = None
    regpos = 0

    for pos in range(0, len(mtc)):
        if regpos == len(reg):
            return False
        if reg[regpos] == '.': # matches any and all character
            regpos += 1 
        elif reg[regpos] == '*': # matches 0+ of preceding character
            regchr = reg[regpos + 1]
            if mtc[pos] != regchr:
                regpos += 1
        elif reg[regpos] == mtc[pos]: # not a special character, exact match
            regpos += 1
        else: # it does not match regular expression
            return False

    return True
 
if __name__ == '__main__':
    mtc_str = 'aa'
    reg_ex = 'a'
    print("%s matches %s = %s" % (mtc_str, reg_ex, 
                                  regular_expression_matching(mtc_str, reg_ex)))
    
    mtc_str = 'aa'
    reg_ex = 'a*'
    print("%s matches %s = %s" % (mtc_str, reg_ex, 
                                  regular_expression_matching(mtc_str, reg_ex)))
    
    mtc_str = 'ab'
    reg_ex = '.*'
    print("%s matches %s = %s" % (mtc_str, reg_ex, 
                                  regular_expression_matching(mtc_str, reg_ex)))
    
    mtc_str = 'aab'
    reg_ex = 'c*a*b'
    print("%s matches %s = %s" % (mtc_str, reg_ex, 
                                  regular_expression_matching(mtc_str, reg_ex)))
    
    mtc_str = 'mississippi'
    reg_ex = 'mis*is*p*.'
    print("%s matches %s = %s" % (mtc_str, reg_ex, 
                                  regular_expression_matching(mtc_str, reg_ex)))

    mtc_str = "mississippi"
    reg_ex = "mis*is*ip*."
    print("%s matches %s = %s" % (mtc_str, reg_ex, 
                                  regular_expression_matching(mtc_str, reg_ex)))

