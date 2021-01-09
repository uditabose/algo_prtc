#!/usr/local/bin/python3

from typing import *

DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def valid_neighbors(grid: List[List[int]], x: int, y: int) -> List[Tuple[int, int]]:
    neighbors = []
    rows = len(grid)
    cols = len(grid[0])
    for dirn in DIRECTIONS:
        x1 = x + dirn[0]
        y1 = y + dirn[1]
        if (0 <= x1 < rows) and (0 <= y1 < cols):
            neighbors.append((x1, y1))

    return neighbors


def build_island(grid: List[List[int]], x: int, y: int) -> int:
    neighbors = valid_neighbors(grid, x, y)
    # print("{} -> {}".format((x, y), neighbors))
    perimeter = 4
    for nb in neighbors:
        if grid[nb[0]][nb[1]] == 1:
            perimeter -= 1
    # print("{} -> {}".format((x, y), perimeter))
    return perimeter


def island_perimeter(grid: List[List[int]]) -> int:
    """
    https://leetcode.com/problems/island-perimeter/

    Time :
    Space: worst -> O(n * m)
    Note : O(n * m)
    """
    island = set()
    perimeter = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1 and (row, col) not in island:
                island.add((row, col))
                perimeter += build_island(grid, row, col)

    return perimeter


def run():
    grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    # grid = [[1]]
    # grid = [[1,0]]
    print(island_perimeter(grid))


if __name__ == '__main__':
    run()
