#!/usr/local/bin/python3

from typing import List


def calculate_water(left_boundary: int, right_boundary: int, height: List[int]) -> int:
    if left_boundary >= right_boundary:
        return 0

    if right_boundary - left_boundary == 1:
        return 0

    print("calculate_water : left_boundary :", left_boundary)
    print("calculate_water : right_boundary :", right_boundary)
    boundary_height = height[min(left_boundary, right_boundary)]
    water = 0
    for index in range(left_boundary + 1, right_boundary):
        water += abs(height[index] - boundary_height)

    print(water)
    return water


def trapping_rain_water(height: List[int]) -> int:
    """
    https://leetcode.com/problems/trapping-rain-water/

    Time :
    Space:
    Note :

    idea is keep 2 pointers
      - left_boundary

      if height[current_index] >= left_high_index:
          calculate_water(left_high_index, current_index)
          left_boundary = current_index
    """

    if len(height) < 2:
        return 0

    left_boundary = 0
    current_index = 1
    minima_index = 0
    total_water = 0
    while current_index < len(height):
        if current_index == len(height) - 1:
            pass # add logic

        if height[left_boundary] <= height[current_index]:
            if height[left_boundary] != 0:
                total_water += calculate_water(left_boundary, current_index, height)
            left_boundary = current_index
        # else:
            # print("left_boundary_at :", left_boundary)
            # print("right_boundary_at :", current_index)

        current_index += 1
    return total_water


def assert_equal(found, expected):
    return found == expected


def run():
    print("-----------")
    # print(assert_equal(trapping_rain_water([0, 1]), 0))
    # print("-----------")
    # print(assert_equal(trapping_rain_water([0, 0, 0]), 0))
    # print("-----------")
    # print(assert_equal(trapping_rain_water([1, 1, 1]), 0))
    # print("-----------")
    # print(assert_equal(trapping_rain_water([1, 2, 3]), 0))
    # print("-----------")
    # print(assert_equal(trapping_rain_water([3, 2, 1]), 0))
    # print("-----------")
    # print(assert_equal(trapping_rain_water([3, 2, 1, 0, 1, 2, 3]), 9))
    # print("-----------")
    print(assert_equal(trapping_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6))
    # print("-----------")


if __name__ == '__main__':
    run()