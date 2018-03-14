
def rotate_matrix_90(matrix):
    '''
    1.7 rotating a N*N matrix by 90 degrees, O(N^2)
    NOT WORKING!!!
    '''
    mat_count = len(matrix)
    max_row = mat_count
    row = 0; col = 0
    while row < mat_count:
        while col < mat_count:
            orig_row, orig_col = row, col
            orig_val = matrix[row][col]
            while True:
                n_row, n_col = col, (mat_count - 1) - row
                print("(%d, %d) -> (%d, %d)" % (row, col, n_row, n_col))

                o_val = matrix[n_row][n_col]
                print("%s -> %s" % (o_val, orig_val))

                matrix[n_row][n_col] = orig_val
                orig_val = o_val

                if n_row == orig_row:
                    break
                else:
                    row, col = n_row, n_col
            col += 1
        row += 1
        col += 1
    return matrix

def run():
    matrix = [['a', 'b', 'c'],
              ['d', 'e', 'f'],
              ['g', 'h', 'i']]
    n_matrix = rotate_matrix_90(matrix)
    print(n_matrix)

if __name__ == '__main__':
    run()