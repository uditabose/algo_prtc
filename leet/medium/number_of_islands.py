#!/usr/local/bin/python3

def valid_neighbor(i, j, grid):
    if i < 0 or j < 0:
        return None
    if i >= len(grid):
        return None
    if j >= len(grid[0]):
        return None

    return (i, j)

def get_node(node, grid):
    if node != None:
        return grid[node[0]][node[1]]

def get_node_visit(node, grid_visit):
    if node != None:
        return grid_visit[node[0]][node[1]]
    return False

def add_to_islands(node, island_queue, grid, grid_visit):
    if get_node(node, grid) == "1" and get_node_visit(node, grid_visit) == False:
        island_queue.append(node)

def is_islan_end(nodes, grid):
    node_ns = [get_node(node, grid) for node in nodes]
    return False if "1" in node_ns else True

def find_island(node, grid, grid_visit):
    print("find_island : ", node)
    if get_node_visit(node, grid_visit):
        return 0

    if get_node(node, grid) != "1":
        return 0

    island_queue = []
    island_queue.append(node)
    island_size = 0

    while len(island_queue) > 0:
        island_size += 1
        a_node = island_queue.pop()
        x = a_node[0]
        y = a_node[1]
        grid_visit[x][y] = True

        top = valid_neighbor(x - 1, y, grid)
        bottom = valid_neighbor(x + 1, y, grid)
        left = valid_neighbor(x, y - 1, grid)
        right = valid_neighbor(x, y + 1, grid)

        islan_end = is_islan_end([top, bottom, left, right], grid)

        if islan_end:
            break

        add_to_islands(top, island_queue, grid, grid_visit)
        add_to_islands(bottom, island_queue, grid, grid_visit)
        add_to_islands(left, island_queue, grid, grid_visit)
        add_to_islands(right, island_queue, grid, grid_visit)

    return 1 if island_size > 0 else 0


def number_of_islands(grid):
    """
    https://leetcode.com/problems/number-of-islands/

    Time :
    Space:
    Note :
    """
    grid_visit = [[False for ch in range(len(grid[0]))] for ch in range(len(grid))]
    island_count = 0
    island_queue = []

    for i, row in enumerate(grid):
        for j, what in enumerate(grid[i]):
            island_count += find_island((i, j), grid, grid_visit)

    return island_count

def run():
    # grid = [
    #             ["1","1","1","1","0"],
    #             ["1","1","0","1","0"],
    #             ["1","1","0","0","0"],
    #             ["0","0","0","0","0"]
    #         ]
    # grid = [
    #             ["1","1","0","0","0"],
    #             ["1","1","0","0","0"],
    #             ["0","0","1","0","0"],
    #             ["0","0","0","1","1"]
    #         ]
    # grid = [
    #             ["1","1","0","0","0"],
    #             ["1","1","0","0","0"],
    #             ["0","0","0","0","0"],
    #             ["0","0","0","0","1"]
    #         ]
    print("islands ", number_of_islands(grid))


if __name__ == '__main__':
    run()
