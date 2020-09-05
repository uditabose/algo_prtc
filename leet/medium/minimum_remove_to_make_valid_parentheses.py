#!/usr/local/bin/python3

def pop_till_open(wstack, last_open, ret_st):
    while True:
        c = wstack.pop()
        ret_st =

    return ret_st

def minimum_remove_to_make_valid_parentheses(s: str) -> str:
    """
    https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

    Time :
    Space:
    Note :
    """
    wstack = []
    ret_st = ""
    last_open = 0
    for i, c in s:
        wstack.append(c)
        elif c == ')':
            pop_till_open(wstack, ret_st)


def run():
    print(minimum_remove_to_make_valid_parentheses("lee(t(c)o)de)"))
    print(minimum_remove_to_make_valid_parentheses("a)b(c)d"))
    print(minimum_remove_to_make_valid_parentheses("))(("))
    print(minimum_remove_to_make_valid_parentheses("(a(b(c)d)"))
    print(minimum_remove_to_make_valid_parentheses("lee((tcode"))


if __name__ == '__main__':
    run()
