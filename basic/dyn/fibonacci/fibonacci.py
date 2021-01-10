from dynamic import Dynamic
from typing import List


class Fibonacci(Dynamic):
    """
    Fib(n) = Fib(n-1) + Fib(n-2), for n > 1

    Given that: Fib(0) = 0, and Fib(1) = 1
    """

    def __init__(self, fib: int):
        self.fib = fib

    def bruteforce(self):
        return self.__recurse__(self.fib)

    def __recurse__(self, n: int):
        if n < 2:
            return n
        return self.__recurse__(n - 1) + self.__recurse__(n - 2)

    def topdown(self):
        memo = [-1 for i in range(0, self.fib + 1)]
        memo[0] = 0
        memo[1] = 1

        return self.__recurse_memo__(self.fib, memo)

    def __recurse_memo__(self, n: int, memo: List[int]):
        if n < 2:
            return memo[n]

        if memo[n] >= 0:
            return memo[n]

        memo[n] = self.__recurse_memo__(n - 1, memo) + self.__recurse_memo__(n - 2, memo)
        return memo[n]

    def bottomup(self):
        table = [-1 for i in range(0, self.fib + 1)]
        table[0] = 0
        table[1] = 1

        for n in range(2, self.fib + 1):
            table[n] = table[n - 1] + table[n - 2]

        return table[self.fib]


if __name__ == '__main__':
    fibonacci = Fibonacci(6)
    fibonacci.all_result()
