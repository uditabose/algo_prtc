def print_matrix(matrix):
    for row in matrix:
        print(row)
    print('---------')

def zero_out(matrix, ridx, cidx):
    for i in range(0, len(matrix)):
        row = matrix[i]
        for j in range(0, len(matrix[0])):
            if i == ridx or j == cidx:
                matrix[i][j] = 0

def zeroing_matrix(matrix):
    '''
    1.8 zero out the row/column in which a 0 value is
    NOT WORKING
    '''
    copy_mat = []
    copy_mat.append(matrix)
    print(len(copy_mat), len(copy_mat[0]))
    
    for i in range(0, len(matrix)):
        row = matrix[i]

        if 0 in row:
            j = row.index(0)
            zero_out(copy_mat, i, j)
        else:
            continue
    return copy_mat

def run():
    matrix = [[1,2,3], [0, 29, 3], [25, 4, 7]]
    print_matrix(matrix)
    print_matrix(zeroing_matrix(matrix))

    print('==========')
    #matrix = [[1,2,3], [23, 0, 9], [34, 56, 90], [0, 8, 6]]
    #print_matrix(matrix)
    #print('---------')
    #print_matrix(zeroing_matrix(matrix))

if __name__ == '__main__':
    run()