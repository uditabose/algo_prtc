

def min_subset_sum_difference_bruteforce_recursive(num_arr, curr_index, sum_with, sum_without):
    if curr_index >= len(num_arr):
        return abs(sum_with - sum_without)

    diff_with = min_subset_sum_difference_bruteforce_recursive(num_arr, curr_index + 1, sum_with + num_arr[curr_index], sum_without)
    diff_without = min_subset_sum_difference_bruteforce_recursive(num_arr, curr_index + 1, sum_with, sum_without + num_arr[curr_index])
    return min(diff_with, diff_without)

def min_subset_sum_difference_bruteforce(num_arr):
    # we start from beginning and carry out calculating sum till the last index
    # 2 sums, with curr_index, without curr_index

    return min_subset_sum_difference_bruteforce_recursive(num_arr, 0, 0, 0)


def main():
    n1 = [1, 2, 3, 9]
    n2 = [1, 2, 7, 1, 5]
    n3 = [1, 3, 100, 4]
    print(min_subset_sum_difference_bruteforce(n1))
    print(min_subset_sum_difference_bruteforce(n2))
    print(min_subset_sum_difference_bruteforce(n3))


if __name__ == "__main__":
    main()