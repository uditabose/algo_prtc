#!/usr/local/bin/python3

from typing import *


def valid_neighbors(rows: int, cols: int, x: int, y: int) -> Set[Tuple[int, int]]:
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    neighbors = set()
    for dirn in directions:
        x1 = int(x) + dirn[0]
        y1 = int(y) + dirn[1]
        if (0 <= x1 < rows) and (0 <= y1 < cols):
            neighbors.add((x1, y1))

    return neighbors


def number_of_islands_ii(m: int, n: int, positions: List[List[int]]):
    neighbors = dict()  # all possible neighbors
    island_count = []  # island counts created at every step
    for idx, position in enumerate(positions):
        x, y = position
        pos_tuple = (x, y)
        new_neighbors = valid_neighbors(m, n, x, y)
        new_neighbors.add(pos_tuple)

        print("new_neighbors : {}".format(neighbors))

        # base case, for
        if len(island_count) == 0:
            island_count.append(1)
        else:
            nb_of = -1
            for key in neighbors:
                if pos_tuple in neighbors[key]:
                    nb_of += 1
            icount = island_count[idx - 1] - nb_of
            icount = icount if icount > 0 else 1
            island_count.append(icount)

        neighbors[pos_tuple] = new_neighbors

    return island_count


def run():
    m = 3
    n = 3
    positions = [[0, 0], [0, 1], [1, 2], [2, 1]]

    # m = 2
    # n = 2
    # positions = [[0, 0], [1, 1], [0, 1]]

    print(number_of_islands_ii(m, n, positions))


if __name__ == '__main__':
    run()
