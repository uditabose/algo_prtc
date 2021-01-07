#!/usr/local/bin/python3

def add_strings(num1: str, num2: str) -> str:
    """
    https://leetcode.com/problems/add-strings/

    Time :
    Space:
    Note :
    """

    if num1 is None or len(num1) == 0:
        return num2

    if num2 is None or len(num2) == 0:
        return num1

    add_str = ""
    carry = 0
    i = len(num1) - 1
    j = len(num2) - 1
    while i >= 0 or j >= 0:
        x = int(num1[i]) if i >= 0 else 0
        y = int(num2[j]) if j >= 0 else 0
        sum = (x + y + carry) % 10
        carry = int((x + y + carry) / 10)
        add_str = str(sum) + add_str
        i -= 1
        j -= 1

    if carry != 0:
        add_str = str(carry) + add_str

    return add_str


def run():
    print(add_strings("98", "7"))


if __name__ == '__main__':
    run()
