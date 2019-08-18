
def subset_sum_bruteforce_recursive(arr, summ, curr_idx):
    if curr_idx >= len(arr):
        return False

    if summ == 0 or arr[curr_idx] == summ:
        return True

    if arr[curr_idx] < summ:
        if subset_sum_bruteforce_recursive(arr, summ - arr[curr_idx], curr_idx + 1):
            return True
    return subset_sum_bruteforce_recursive(arr, summ, curr_idx + 1)

def subset_sum_bruteforce(arr, summ):
    if summ == 0:
        return True
    return subset_sum_bruteforce_recursive(arr, summ, 0)

############

def subset_sum_topdown_recursive(arr, summ, memo, curr_idx):
    if curr_idx >= len(arr):
        return False

    if summ == 0 or arr[curr_idx] == summ:
        memo[curr_idx][summ] = True
        return True

    if arr[curr_idx] <= summ:
        if subset_sum_topdown_recursive(arr, summ - arr[curr_idx], memo, curr_idx + 1):
            memo[curr_idx][summ] = True
            return True

    memo[curr_idx][summ] = subset_sum_topdown_recursive(arr, summ, memo, curr_idx + 1)
    return memo[curr_idx][summ]

def subset_sum_topdown(arr, summ):
    if summ == 0:
        return True

    memo = [[False for i in range(summ + 1)] for j in range(len(arr))]
    return subset_sum_topdown_recursive(arr, summ, memo, 0)

############

def subset_sum_bottomup(arr, summ):
    if summ == 0:
        return True

    table = [[False for i in range(summ + 1)] for j in range(len(arr))]

    for i in range(len(arr)):
        table[i][0] = True

    for i in range(0, summ + 1):
        table[0][i] = arr[0] == i

    # process all subsets for all sums
    for i in range(1, len(arr)):
        for s in range(1, summ + 1):
            # if we can get the sum 's' without the number at index 'i'
            if table[i - 1][s]:
                table[i][s] = table[i - 1][s]
            elif s >= arr[i]:
                # else include the number and see if we can find a subset to get the remaining sum
                table[i][s] = table[i - 1][s - arr[i]]

    # the bottom-right corner will have our answer.
    return table[len(arr) - 1][summ]


############


def main():
    arr1 = [1, 2, 3, 7]; sum1 = 6
    arr2 = [1, 2, 7, 1, 5]; sum2 = 10
    arr3 = [1, 3, 4, 8]; sum3 = 6
    print("---- bruteforce ----")
    print(subset_sum_bruteforce(arr1, sum1))
    print(subset_sum_bruteforce(arr2, sum2))
    print(subset_sum_bruteforce(arr3, sum3))

    print("---- topdown ----")
    print(subset_sum_topdown(arr1, sum1))
    print(subset_sum_topdown(arr2, sum2))
    print(subset_sum_topdown(arr3, sum3))

    print("---- bottomup ----")
    print(subset_sum_bottomup(arr1, sum1))
    print(subset_sum_bottomup(arr2, sum2))
    print(subset_sum_bottomup(arr3, sum3))

if __name__ == "__main__":
    main()