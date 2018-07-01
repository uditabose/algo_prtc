def is_dest(point, dest, maze):
    row, col = point[0], point[1]
    #print("row : %d :: col : %d" % (row, col))
    if row == dest[0] and col == dest[1]:
        return True
    else:
        return False

def in_range(point, dest, maze):
    row, col = point[0], point[1]
    if row < 0 or row >= len(maze):
        return False
    if col < 0 or col >= len(maze[0]):
        return False

    return True

def is_wall(point, dest, maze): 
    row, col = point[0], point[1]
    if not in_range(point, dest, maze):
        return True
    
    if maze[row][col] == 1:
        return True
    else:
        return False

def the_maze(maze, start, dest):
    '''
    There is a ball in a maze with empty spaces and walls. 
    The ball can go through empty spaces by rolling up, down, 
    left or right, but it won't stop rolling until hitting a wall. 
    When the ball stops, it could choose the next direction.
    Given the ball's start position, the destination and the maze, 
    determine whether the ball could stop at the destination.

    The maze is represented by a binary 2D array. 1 means the 
    wall and 0 means the empty space. You may assume that the 
    borders of the maze are all walls. The start and destination 
    coordinates are represented by row and column indexes.

    Example 1

    Input 1: a maze represented by a 2D array

    0 0 1 0 0
    0 0 0 0 0
    0 0 0 1 0
    1 1 0 1 1
    0 0 0 0 0

    Input 2: start coordinate (rowStart, colStart) = (0, 4)
    Input 3: destination coordinate (rowDest, colDest) = (4, 4)

    Output: true
    Explanation: One possible way is : 
    left -> down -> left -> down -> right -> down -> right.

    Example 2

    Input 1: a maze represented by a 2D array

    0 0 1 0 0
    0 0 0 0 0
    0 0 0 1 0
    1 1 0 1 1
    0 0 0 0 0

    Input 2: start coordinate (rowStart, colStart) = (0, 4)
    Input 3: destination coordinate (rowDest, colDest) = (3, 2)

    Output: false
    Explanation: There is no way for the ball to stop at the destination.

    Note:
    There is only one ball and one destination in the maze.
    Both the ball and the destination exist on an empty space, 
    and they will not be at the same position initially.
    The given maze does not contain border (like the red rectangle 
    in the example pictures), but you could assume the border of 
    the maze are all walls.
    The maze contains at least 2 empty spaces, and both the width 
    and height of the maze won't exceed 100.

    https://leetcode.com/problems/the-maze/description/

    Time :
    Space:
    Note :
    '''
    if maze == None or len(maze) == 0:
        return False

    if start == None or len(start) < 2:
        return False

    if dest == None or len(dest) < 2:
        return False

    # points
    #  (x-1, y) <- (x, y) -> (x+1, y) 
    #                | 
    #             (x, y+1)

    # row-col
    #  (row, col-1) <- (row, col) -> (row, col+1) 
    #                       | 
    #                 (row+1, col)

    #print("maze row : %d :: maze col : %d" % (len(maze), len(maze[0])))
    pos_stack = [tuple(start)]
    pos_map = set([])
    pos_map.add(tuple(start))

    while len(pos_stack) > 0:
        point = pos_stack.pop()
        
        # connected points
        l_point = (point[0], point[1] - 1)
        r_point = (point[0], point[1] + 1)
        d_point = (point[0] + 1, point[1])
        u_point = (point[0] - 1, point[1])

        if is_dest(point, dest, maze):
            return (is_wall(d_point, dest, maze) 
                    or is_wall(r_point, dest, maze) 
                    or is_wall(l_point, dest, maze)
                    or is_wall(u_point, dest, maze))
        else:
            if not is_wall(l_point, dest, maze) and not l_point in pos_map:
                pos_map.add(l_point)
                pos_stack.append(l_point)

            if not is_wall(r_point, dest, maze) and  not r_point in pos_map:
                pos_map.add(r_point)
                pos_stack.append(r_point)

            if not is_wall(d_point, dest, maze) and  not d_point in pos_map:
                pos_map.add(d_point)
                pos_stack.append(d_point)

    #print(pos_map)
    return False
        
def run():
    maze = [[0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [1, 1, 0, 1, 1],
            [0, 0, 0, 0, 0]]
    start = [0, 4]
    dest = [4, 4]
    print("there is a way %s" % str(the_maze(maze, start, dest)))

    start = [0, 4]
    dest =  [3, 2]
    print("there is a way %s" % str(the_maze(maze, start, dest)))

if __name__ == '__main__':
    run()

