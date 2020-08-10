def get_max_profit(stock_prices_yesterday):
    '''
    https://www.interviewcake.com/question/python/stock-price

    First, I wanna know how much money I could have made 
    yesterday if I'd been trading Apple stocks all day.

    So I grabbed Apple's stock prices from yesterday 
    and put them in a list called stock_prices_yesterday, where:

    The indices are the time (in minutes) past trade 
    opening time, which was 9:30am local time.
    The values are the price (in US dollars) of one share 
    of Apple stock at that time.
    So if the stock cost $500 at 10:30am, that means 
    stock_prices_yesterday[60] = 500.

    Write an efficient function that takes stock_prices_yesterday 
    and returns the best profit I could have made from 
    one purchase and one sale of one share of Apple stock yesterday.
    '''
    alen = len(stock_prices_yesterday)
    i = 0; j = alen - 1
    min_on_left = stock_prices_yesterday[0]
    max_on_right = stock_prices_yesterday[-1]
    max_idx = alen - 1
    min_idx = 0
    while i < alen and max_idx > min_idx:
        if stock_prices_yesterday[i] < min_on_left:
            min_on_left = stock_prices_yesterday[i]
            min_idx = i

        if stock_prices_yesterday[j] > max_on_right:
            max_on_right = stock_prices_yesterday[j]
            max_idx = j

        i += 1
        j -= 1

    return (max_on_right - min_on_left)

if __name__ == '__main__':
    print("Profit is %d" % get_max_profit([10, 7, 5, 8, 11, 9]))
    print ("\n-------------------------------------\n")
    print("Profit is %d" % get_max_profit([10, 9, 8, 7, 6, 5, 4]))
    print ("\n-------------------------------------\n")
    print("Profit is %d" % get_max_profit([1, 3, 4, 5, 6, 7, 8]))
