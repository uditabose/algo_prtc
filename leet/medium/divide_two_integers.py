#!/usr/local/bin/python3

def divide_two_integers_doubled_up(dividend, divisor):
    """
    https://leetcode.com/problems/divide-two-integers/

    Time :
    Space:
    Note :
    """
    div_map = {}

    mod_divisor = divisor
    if mod_divisor < 1:
        mod_divisor *= -1

    mod_dividend = dividend
    if mod_dividend < 1:
        mod_dividend *= -1

    rest = mod_dividend
    result = 1
    while rest > mod_divisor:
        div_map[mod_divisor] = result
        rest -= mod_divisor
        mod_divisor += mod_divisor
        result += result

    mod_divisor = divisor
    if mod_divisor < 1:
        mod_divisor *= -1

    rest_result = 0
    for k, v in div_map.items():
        if rest - k < mod_divisor:
            break
        else:
            rest_result = v

    return result + rest_result


def divide_two_integers_repeated_substraction(dividend, divisor):
    """
    https://leetcode.com/problems/divide-two-integers/

    Time :
    Space:
    Note :
    """
    mod_divisor = divisor
    if mod_divisor < 1:
        mod_divisor *= -1

    mod_dividend = dividend
    if mod_dividend < 1:
        mod_dividend *= -1

    rest = mod_dividend
    result = 0
    while rest > mod_divisor:
        rest -= mod_divisor
        result += 1

    if divisor < 1:
        result *= -1
    if dividend < 1:
        result *= -1

    return result

def run():
    print(divide_two_integers_repeated_substraction(10, 3))
    print(divide_two_integers_repeated_substraction(7, -3))

    print("-------------------")

    print(divide_two_integers_doubled_up(10, 3))
    print(divide_two_integers_doubled_up(7, -3))


if __name__ == '__main__':
    run()
