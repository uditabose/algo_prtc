
def toeplitz_matrix(matrix):
    '''
    A matrix is Toeplitz if every diagonal from top-left 
    to bottom-right has the same element.

    Now given an M x N matrix, return True if and only 
    if the matrix is Toeplitz.
 
    Example 1:

    Input:
    matrix = [
      [1,2,3,4],
      [5,1,2,3],
      [9,5,1,2]
    ]
    Output: True
    Explanation:
    In the above grid, the diagonals are:
    "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
    In each diagonal all elements are the same, so the answer is True.
    
    Example 2:

    Input:
    matrix = [
      [1,2],
      [2,2]
    ]
    Output: False
    Explanation:
    The diagonal "[1, 2]" has different elements.

    https://leetcode.com/problems/toeplitz-matrix/description/

    Time :
    Space:
    Note :

    1. First  - row == col
    2. Second - (0, M-2), (, )
    '''
    if matrix == None or len(matrix) == 0:
        return False

    if len(matrix) == 1:
        return True

    diagonal = set([])
    i = 0
    j = 0

    while i < len(matrix) and j < len(matrix[0]):
        diagonal.add(matrix[i][j])
        if len(diagonal) > 0:
            return False

        if i+1 == len(matrix):
            i = 0
            j = 


def run():
    pass

if __name__ == '__main__':
    run()

