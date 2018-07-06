#!/usr/local/bin/python3

def get_valid_neighbours(row, col, board):
    '''
    row-col:  
      (row-1, col-1) -- (row-1, col) -- (row-1, col+1)
                           |
        (row, col-1) -- (row, col)   -- (row, col+1)
                           |
      (row+1, col-1) -- (row+1, col) -- (row+1, col+1)  
   
    '''
    neighbours = []
    if row - 1 >= 0:
        neighbours.append((row - 1, col))
        if col - 1 >= 0:
            neighbours.append((row - 1, col - 1))
        if col + 1 < len(board[0]):
            neighbours.append((row - 1, col + 1))

    if col - 1 >= 0:
        neighbours.append((row, col - 1))
    if col + 1 < len(board[0]):
        neighbours.append((row, col + 1))

    if row + 1 < len(board):
        neighbours.append((row + 1, col))
        if col - 1 >= 0:
            neighbours.append((row + 1, col - 1))
        if col + 1 < len(board[0]):
            neighbours.append((row + 1, col + 1))

    return neighbours

def get_updated_value(row, col, board, neighbours):
    '''
    sum neighbours
        a. sum < 2  ==> flip 1 to 0
        b. sum > 3  ==> flip 1 to 0
        c. sum == 3 ==> flip 0 to 1
    '''
    curr_val = board[row][col]
    neighbour_sum = 0
    for point in neighbours:
        neighbour_sum += board[point[0]][point[1]]

    if neighbour_sum < 2 and curr_val == 1:
        return 0
    elif neighbour_sum == 3 and curr_val == 0:
        return 1
    elif neighbour_sum > 3 and curr_val == 1:
        return 0
    else:
        return curr_val

def game_of_life(board):
    '''
    According to the Wikipedia's article: 
    "The Game of Life, also known simply as Life, is a 
    cellular automaton devised by the British mathematician 
    John Horton Conway in 1970."

    Given a board with m by n cells, each cell has an 
    initial state live (1) or dead (0). Each cell interacts 
    with its eight neighbors (horizontal, vertical, diagonal) 
    using the following four rules (taken from the above 
    Wikipedia article):

    > Any live cell with fewer than two live neighbors dies, 
    as if caused by under-population.
    
    > Any live cell with two or three live neighbors lives on 
    to the next generation.
    
    > Any live cell with more than three live neighbors dies, 
    as if by over-population.
    
    > Any dead cell with exactly three live neighbors becomes 
    a live cell, as if by reproduction.
    
    Write a function to compute the next state (after one update) 
    of the board given its current state. The next state is 
    created by applying the above rules simultaneously to 
    every cell in the current state, where births and deaths 
    occur simultaneously.

    Example:

    Input: 
    [
      [0,1,0],
      [0,0,1],
      [1,1,1],
      [0,0,0]
    ]
    Output: 
    [
      [0,0,0],
      [1,0,1],
      [0,1,1],
      [0,1,0]
    ]
    Follow up:

    1. Could you solve it in-place? Remember that the board 
    needs to be updated at the same time: You cannot update 
    some cells first and then use their updated values to 
    update other cells.
    
    2. In this question, we represent the board using a 2D array. 
    In principle, the board is infinite, which would cause 
    problems when the active area encroaches the border of 
    the array. How would you address these problems?
    
    https://leetcode.com/problems/game-of-life/description/

    Time : O(N^2)
    Space: O(N^2)
    Note :
    
    points:
      (x-1, y-1) -- (x, y-1) -- (x+1, y-1)
                       |
        (x-1, y) -- (x, y)   -- (x+1, y)
                       |
      (x-1, y+1) -- (x, y+1) -- (x+1, y+1)

    row-col:  
      (row-1, col-1) -- (row-1, col) -- (row-1, col+1)
                           |
        (row, col-1) -- (row, col)   -- (row, col+1)
                           |
      (row+1, col-1) -- (row+1, col) -- (row+1, col+1)  

    
    1. get valid neighbours
    2. sum neighbours
        a. sum < 2  ==> flip 1 to 0
        b. sum > 3  ==> flip 1 to 0
        c. sum == 3 ==> flip 0 to 1
    '''
    
    if board == None or len(board) == 0:
        return board

    new_board = []
    for row in range(0, len(board)):
        updated_row = []
        for col in range(0, len(board[row])):
            neighbours = get_valid_neighbours(row, col, board)
            #print("(%d, %d)" % (row, col))
            #print(neighbours)
            updated_val = get_updated_value(row, col, board, neighbours)
            updated_row.append(updated_val)
        new_board.append(updated_row)

    #print('------------------')
    return new_board

def run():
    board = [[0,1,0],
             [0,0,1],
             [1,1,1],
             [0,0,0]]
    flipped_board = game_of_life(board)
    print(flipped_board)

    # [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
    # [[0,0,0],   [1,0,1],   [0,1,1],   [0,1,0]

if __name__ == '__main__':
    run()

