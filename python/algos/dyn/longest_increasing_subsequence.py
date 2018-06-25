def longest_increasing_subsequence(num_arr):
    if num_arr == None or len(num_arr) == 0:
        return None, 0, 0

    nlen = len(num_arr)
    num_matrix = [[False] * nlen for n in range(nlen)]
    len_arr = [1] * nlen

    for i in range(0, nlen):
        num = num_arr[i]
        #print("num[%d] = %d" % (i, num))
        num_matrix[i][i] = True
        for j in range(0, i):
            if num > num_arr[j] :
                num_matrix[j][i] = True
                len_arr[i] = max(len_arr[i], len_arr[j] + 1)

        #print(num_matrix[i])
        #print(len_arr)

    max_len = max(len_arr)
    max_index = len_arr.index(max_len) 

    return num_matrix, max_index, max_len

if __name__ == '__main__':
    print(longest_increasing_subsequence([5, 2, 8, 6, 3, 6, 9, 7]))