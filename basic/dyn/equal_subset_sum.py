
def equal_subset_sum_bruteforce_recursive(num_arr, half_sum, curr_idx):
    if half_sum == 0:
        return True

    nums_len = len(num_arr)
    if nums_len == 0 or curr_idx >= nums_len:
        return False

    # sum with the index
    if num_arr[curr_idx] <= half_sum:
        if equal_subset_sum_bruteforce_recursive(num_arr, half_sum - num_arr[curr_idx], curr_idx + 1):
            return True
    # sum without the index
    return equal_subset_sum_bruteforce_recursive(num_arr, half_sum, curr_idx + 1)


def equal_subset_sum_bruteforce(num_arr):
    whole_sum = sum(num_arr)
    if whole_sum == 0 or whole_sum % 2 != 0:
        return False
    return equal_subset_sum_bruteforce_recursive(num_arr, whole_sum / 2, 0)


def equal_subset_sum_topdown_recursive(num_arr, half_sum, memo, curr_idx):
    if half_sum == 0:
        return 1

    nums_len = len(num_arr)
    if nums_len == 0 or curr_idx >= nums_len:
        return -1

    if num_arr[curr_idx] <= half_sum:
        if equal_subset_sum_topdown_recursive(num_arr, half_sum - num_arr[curr_idx], memo, curr_idx + 1) == 1:
            memo[curr_idx][half_sum] = 1
            return 1

    memo[curr_idx][half_sum] = equal_subset_sum_topdown_recursive(num_arr, half_sum, memo, curr_idx + 1)
    return memo[curr_idx][half_sum]


def equal_subset_sum_topdown(num_arr):
    whole_sum = sum(num_arr)
    if whole_sum == 0 or whole_sum % 2 != 0:
        return False

    half_sum = int(whole_sum / 2)
    memo = [[-1 for i in range(1 + half_sum)] for j in range(len(num_arr))]
    return True if equal_subset_sum_topdown_recursive(num_arr, half_sum, memo, 0) == 1 else False


def equal_subset_sum_bottomup(num_arr):
    whole_sum = sum(num_arr)
    if whole_sum == 0 or whole_sum % 2 != 0:
        return False

    half_sum = int(whole_sum / 2)
    table = [[False for i in range(1 + half_sum)] for j in range(len(num_arr))]

    for ts in range(len(num_arr)):
        table[ts][0] = True

    for i in range(1, len(table)):
        for j in range(1, 1 + half_sum):
            if table[i - 1][j]:
                table[i][j] = table[i - 1][j]
            elif j >= num_arr[i]:  # else if we can find a subset to get the remaining sum
                table[i][j] = table[i - 1][j - num_arr[i]]

    return table[len(num_arr) - 1][half_sum]


def main():
    num_arr_1 = [1, 2, 3, 4]
    num_arr_2 = [1, 1, 3, 4, 7]
    num_arr_3 = [2, 3, 4, 6]

    print(" ---- bruteforce ----")
    print(equal_subset_sum_bruteforce(num_arr_1))
    print(equal_subset_sum_bruteforce(num_arr_2))
    print(equal_subset_sum_bruteforce(num_arr_3))
    print(" ---- topdown ----")
    print(equal_subset_sum_topdown(num_arr_1))
    print(equal_subset_sum_topdown(num_arr_2))
    print(equal_subset_sum_topdown(num_arr_3))
    print(" ---- bottomup ----")
    print(equal_subset_sum_bottomup(num_arr_1))
    print(equal_subset_sum_bottomup(num_arr_2))
    print(equal_subset_sum_bottomup(num_arr_3))


if __name__ == "__main__":
    main()