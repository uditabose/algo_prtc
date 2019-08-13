
def calculate_top_down_fibonacci(n):
    memoize = [-1 for x in range(n + 1)]
    return top_down_fibonacci_recur(memoize, n)

def top_down_fibonacci_recur(memoize, n):
    if n < 2:
        return n

    # subproblem is already calculated
    if memoize[n] >= 0:
        return memoize[n]

    memoize[n] = top_down_fibonacci_recur(memoize, n - 1) + top_down_fibonacci_recur(memoize, n - 2)

    return memoize[n]

def calculate_bottom_up_fibonacci(n):
    fib_table = [0, 1]
    for x in range(2, n + 1):
        fib_table.append(fib_table[x - 1] + fib_table[x - 2])

    return fib_table[n]

def main():
    print("TopDown")
    print("5th # " + str(calculate_top_down_fibonacci(5)))
    print("15th # " + str(calculate_top_down_fibonacci(15)))

    print("BottomUp")
    print("5th # " + str(calculate_bottom_up_fibonacci(5)))
    print("15th # " + str(calculate_bottom_up_fibonacci(15)))

if __name__ == "__main__":
    main()
