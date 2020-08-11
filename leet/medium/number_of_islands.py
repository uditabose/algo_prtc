#!/usr/local/bin/python3

def validate_neighbor(i, j, grid):
    if i < 0 or j < 0:
        return None
    if i >= len(grid):
        return None
    if j >= len(grid[0]):
        return None

    return (i, j)

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
            if grid_visit[i][j]:
                continue
            grid_visit[i][j] = True

            top = validate_neighbor(i - 1, j, grid)
            bottom = validate_neighbor(i + 1, j, grid)
            left = validate_neighbor(i, j - 1, grid)
            right = validate_neighbor(i, j + 1, grid)

            if int(what) == 1:
                island_queue.append((i, j))

                top_n = bottom_n = left_n = right_n = None
                if top != None:
                    top_n = grid[top[0]][top[1]]

                if bottom != None:
                    bottom_n = grid[bottom[0]][bottom[1]]

                if left != None:
                    left_n = grid[left[0]][left[1]]

                if right != None:
                    right_n = grid[right[0]][right[1]]

                print(top_n, bottom_n, left_n, right_n)
                if top_n != "1" and bottom != "1" and left != "1" and right != "1":
                    island_count += 1
                    print(island_queue)
                    island_queue.clear()

                if bottom_n == 1:
                    island_queue.append(bottom)

                if left_n == 1:
                    island_queue.append(left)

                if left_n == 1:
                    island_queue.append(left)

                if right_n == 1:
                    island_queue.append(right)

    print(island_count)


def run():
    # grid = [
    #             ["1","1","1","1","0"],
    #             ["1","1","0","1","0"],
    #             ["1","1","0","0","0"],
    #             ["0","0","0","0","0"]
    #         ]
    grid = [
                ["1","1","0","0","0"],
                ["1","1","0","0","0"],
                ["0","0","1","0","0"],
                ["0","0","0","1","1"]
            ]
    number_of_islands(grid)


if __name__ == '__main__':
    run()
