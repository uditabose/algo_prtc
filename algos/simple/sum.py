# from typing import List, Any

def add(str1: str, str2: str):
    list = []
    carry = 0
    i = len(str1) - 1
    j = len(str2) - 1
    while i >= 0 and j >= 0:
        sum = int(str1[i]) + int(str2[j]) + carry
        carry = int(sum / 10)
        sum = int(sum % 10)
        list.append(sum)
        i -= 1
        j -= 1

    while i >= 0:
        sum = int(str1[i]) + carry
        carry = int(sum / 10)
        sum = int(sum % 10)
        list.append(sum)
        i -= 1

    while j >= 0:
        sum = int(str2[j]) + carry
        carry = int(sum / 10)
        sum = int(sum % 10)
        list.append(sum)
        j -= 1

    if carry > 0:
        list.append(carry)

    result = ''
    while len(list) > 0:
        result += str(list.pop())

    # print(result)
    return result


def assert_equal(found, expected):
    return found == expected


if __name__== '__main__':
    print(assert_equal(add('1', '2'), '3'))
    print(assert_equal(add('10', '20'), '30'))
    print(assert_equal(add('10', '200'), '210'))
    print(assert_equal(add('100', '20'), '120'))
    print(assert_equal(add('99', '1'), '100'))
    print(assert_equal(add('99', '11'), '110'))
    print(assert_equal(add('9342', '57'), '9399'))
    print(assert_equal(add('9342', '59'), '9401'))