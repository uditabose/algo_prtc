def get_max_profit(stock_prices_yesterday):
    '''
    https://www.interviewcake.com/question/java/stock-price
    '''
    alen = len(stock_prices_yesterday)
    i = 0; j = alen - 1
    min_on_left = stock_prices_yesterday[0]
    max_on_right = stock_prices_yesterday[-1]

    while i < alen and j > i:
        min_on_left = min(min_on_left, stock_prices_yesterday[i])
        max_on_right = max(max_on_right, stock_prices_yesterday[j])
        i += 1
        j -= 1

    return (max_on_right - min_on_left)

if __name__ == '__main__':
    print("Profit is %d" % get_max_profit([10, 7, 5, 8, 11, 9]))
    print ("\n-------------------------------------\n")
    print("Profit is %d" % get_max_profit([10, 9, 8, 7, 6, 5, 4]))
    print ("\n-------------------------------------\n")
    print("Profit is %d" % get_max_profit([1, 3, 4, 5, 6, 7, 8]))
