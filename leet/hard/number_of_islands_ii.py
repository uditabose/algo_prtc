#!/usr/local/bin/python3

from typing import *

a
def valid_neighbors(grid: List[List[str]], x: int, y: int) -> List[Tuple[int, int]]:
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    neighbors = []
    rows = len(grid)
    cols = len(grid[0])
    for dirn in directions:
        x1 = int(x) + dirn[0]
        y1 = int(y) + dirn[1]
        if (0 <= x1 < rows) and (0 <= y1 < cols):
            neighbors.append((x1, y1))

    return neighbors


def number_of_islands_ii(m: int, n: int, positions: List[List[int]]):
    """
    https://leetcode.com/problems/number-of-islands-ii/

    Time :
    Space:
    Note :
    """
    pass


def run():
    pass


if __name__ == '__main__':
    run()
