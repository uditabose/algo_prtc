def knapshack_bruteforce_recursive(profits, weights, capacity, curr_index):
    if curr_index >= len(profits):
        return 0

    if capacity <= 0:
        return 0

    profit_with_curr_index = 0
    if weights[curr_index] <= capacity:
        profit_with_curr_index = profits[curr_index] + knapshack_bruteforce_recursive(profits, weights,
                                                                        capacity - weights[curr_index], curr_index + 1)
    profit_without_curr_index = knapshack_bruteforce_recursive(profits, weights, capacity, curr_index + 1)

    return max(profit_with_curr_index, profit_without_curr_index)


def kanapshak_bruteforce(profits, weights, capacity):
    if capacity == 0:
        return 0
    curr_index = 0
    return knapshack_bruteforce_recursive(profits, weights, capacity, curr_index)


def knapshack_topdown_recursive(profits, weights, capacity, curr_index, memo):
    if curr_index >= len(profits):
        return 0

    if capacity <= 0:
        return 0

    if memo[curr_index][capacity] != -1:
        return memo[curr_index][capacity]

    profit_with_curr_index = 0
    if weights[curr_index] <= capacity:
        profit_with_curr_index = profits[curr_index] \
                               + knapshack_topdown_recursive(profits, weights, capacity - weights[curr_index], curr_index + 1, memo)
    profit_without_curr_index = knapshack_topdown_recursive(profits, weights, capacity, curr_index + 1, memo)
    memo[curr_index][capacity] = max(profit_with_curr_index, profit_without_curr_index)

    return memo[curr_index][capacity]


def knapshack_topdown(profits, weights, capacity):
    if capacity == 0:
        return 0
    curr_index = 0

    memo = [[-1 for i in range(capacity + 1)] for j in range(len(profits))]
    return knapshack_topdown_recursive(profits, weights, capacity, curr_index, memo)


def knapshack_bottomup(profits, weights, capacity):
    if capacity == 0:
        return 0
    no_items = len(profits)
    table = [[0 for i in range(capacity + 1)] for j in range(no_items)]

    # for 0 capacity we don't select any item
    for i in range(no_items):
        table[i][0] = 0

    for c in range(0, capacity + 1):
        if weights[0] <= c:
            table[0][c] = profits[0]

    for i in range(1, no_items):
        for c in range(1, capacity + 1):
            profit1, profit2 = 0, 0
            # include the item, if it is not more than the capacity
            if weights[i] <= c:
                profit1 = profits[i] + table[i - 1][c - weights[i]]
            # exclude the item
            profit2 = table[i - 1][c]
            # take maximum
            table[i][c] = max(profit1, profit2)

    # maximum profit will be at the bottom-right corner.
    return table[no_items - 1][capacity]


def main():
    profits = [1, 6, 10, 16]
    weights = [1, 2, 3, 5]
    capacity = 7

    print(" --- kanapshak_bruteforce --- ")
    print(kanapshak_bruteforce(profits, weights, capacity))

    print(" --- knapshack_topdown --- ")
    print(knapshack_topdown(profits, weights, capacity))

    print(" --- kanapshak_bottomup --- ")
    print(knapshack_bottomup(profits, weights, capacity))


if __name__ == "__main__":
    main()
