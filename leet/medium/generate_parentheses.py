#!/usr/local/bin/python3
from typing import List


def make_parentheses(parentheses, n):
    if n == 0:
        return parentheses

    tmp = set([])
    for elem in parentheses:
        tmp.add("(){}".format(elem))
        tmp.add("{}()".format(elem))
        tmp.add("({})".format(elem))

    parentheses.clear()
    parentheses.update(tmp)
    make_parentheses(parentheses, n - 1)


def generate_parentheses(n: int) -> List[str]:
    """
    https://leetcode.com/problems/generate-parentheses/

    Time :
    Space:
    Note :
    """
    if n == 0:
        return ""
    if n == 1:
        return ["()"]

    parentheses = set(["()"])

    make_parentheses(parentheses, n - 1)

    return list(parentheses)


def run():
    print(generate_parentheses(8))


if __name__ == '__main__':
    run()
