#!/usr/local/bin/python3
import string

ALPHA = {i + 1: string.ascii_lowercase[i] for i in range(0, 26)}


def decode_ways(num_str: str) -> int:
    """
    https://leetcode.com/problems/decode-ways/

    Time :
    Space:
    Note :
    """

    if num_str is None:
        return 0

    target = None
    if len(num_str) < 1:
        return 0
    elif len(num_str) == 1:
        return 0 if int(num_str) == 0 else 1
    elif int(num_str) == 0:
        return 0
    else:
        target = str(int(num_str))

    if target is None:
        return 0

    ways = 1
    for i in range(1, len(target)):
        current = target[i]

        if int(current) == 0:
            continue

        cs = int(target[i-1:i+1])
        if cs in ALPHA:
            ways += 1

    return ways


def run():
    print(decode_ways("10"))
    # print(decode_ways("0"))
    # print(decode_ways("1"))
    # print(decode_ways("12"))
    # print(decode_ways("226"))
    # print(decode_ways("666"))
    # print(decode_ways("66"))


if __name__ == '__main__':
    run()
