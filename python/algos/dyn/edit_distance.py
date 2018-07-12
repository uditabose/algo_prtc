def edit_distance(astr, bstr):
    if astr == None or len(astr) == 0:
        return 0

    if bstr == None or len(bstr) == 0:
        return 0

    edit_matrix = [[0] * len(astr) for n in range(len(bstr))]

    for i in range(0, len(astr)):
        for j in range(0, len(bstr)):
            if i == 0:
                edit_matrix[i][j] = j
            elif j == 0:
                edit_matrix[i][j] = i
            elif astr[i] == bstr[j]:
                edit_matrix[i][j] = edit_matrix[i-1][j-1]
            else:
                edit_matrix[i][j] = 1 + min(edit_matrix[i-1][j-1], edit_matrix[i-1][j] , edit_matrix[i][j-1] )
                
    return edit_matrix[len(astr-1)][len(bstr-1)]

if __name__ == '__main__':
    print(edit_distance('snowy', 'sunny'))
    print(edit_distance('potential', 'exponential'))