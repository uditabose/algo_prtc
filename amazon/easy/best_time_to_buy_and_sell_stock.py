#!/usr/local/bin/python3

def best_time_to_buy_and_sell_stock(stock_arr):
    """
    Say you have an array for which the ith element is the
    price of a given stock on day i.

    If you were only permitted to complete at most one
    transaction (i.e., buy one and sell one share of the stock),
    design an algorithm to find the maximum profit.

    Note that you cannot sell a stock before you buy one.

    Example 1:

    Input: [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on
    day 5 (price = 6), profit = 6-1 = 5.
                 Not 7-1 = 6, as selling price needs to be
                 larger than buying price.
    Example 2:

    Input: [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transaction is done,
    i.e. max profit = 0.

    https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

    Time :
    Space:
    Note :
    1. one index starts at 0, buy index, ends at (len-1)
        another starts at 1, sell index, ends at len
    2. min index, max index at higher
    """
    if not stock_arr:
        return 0

    ln = len(stock_arr)

    min_price = stock_arr[0]
    max_diff = 0
    for idx in range(1, len(stock_arr)):
        if stock_arr[idx] < min_price:
            min_price = stock_arr[idx]
        elif max_diff < stock_arr[idx] - min_price:
            max_diff = stock_arr[idx] - min_price

    # print("%d ::: " % (max_diff))
    return max_diff


def run():
    print(best_time_to_buy_and_sell_stock([7, 1, 5, 3, 6, 4]))
    print(best_time_to_buy_and_sell_stock([7, 1]))
    print(best_time_to_buy_and_sell_stock([1, 7]))
    print(best_time_to_buy_and_sell_stock([1, 2, 3, 4, 5]))
    print(best_time_to_buy_and_sell_stock([5, 4, 3, 2, 1]))
    print(best_time_to_buy_and_sell_stock([2, 4, 1]))

    print(best_time_to_buy_and_sell_stock([2, 1, 2, 0, 1]))


if __name__ == '__main__':
    run()
