#!/usr/local/bin/python3

from typing import *


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


def number_of_islands(grid: List[List[str]]):
    """
    https://leetcode.com/problems/number-of-islands/

    Time :
    Space:
    Note :
    """
    island_queue = []
    visited = set()
    islands = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            pos = (row, col)
            # visited.add(pos)
            if grid[row][col] == "0":
                continue

            if pos not in visited:
                island_queue.append(pos)

            while len(island_queue) > 0:
                current = island_queue.pop()
                neighbors = valid_neighbors(grid, current[0], current[1])
                visited.add(current)
                for nb in neighbors:
                    if grid[nb[0]][nb[1]] == "1" and nb not in visited:
                        island_queue.append(nb)
                print("{} -> {}".format(pos, island_queue))

                if len(island_queue) == 0:
                    islands += 1
    return islands


def run():
    grid = [
                ["1","1","1","1","0"],
                ["1","1","0","1","0"],
                ["1","1","0","0","0"],
                ["0","0","0","0","0"]
            ]
    # grid = [
    #             ["1","1","0","0","0"],
    #             ["1","1","0","0","0"],
    #             ["0","0","1","0","0"],
    #             ["0","0","0","1","1"]
    #         ]
    # grid = [
    #     ["1", "1", "0", "0", "0"],
    #     ["1", "1", "0", "0", "0"],
    #     ["0", "0", "0", "0", "0"],
    #     ["0", "0", "0", "0", "1"]
    # ]
    print(number_of_islands(grid))


if __name__ == '__main__':
    run()
