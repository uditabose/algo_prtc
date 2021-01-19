from typing import *
from dynamic import Dynamic


class UnboundedKnapshack(Dynamic):
    def __init__(self, weights: List[int], profits: List[int], capacity: int):
        self.weights = weights
        self.profits = profits
        self.capacity = capacity

    def bruteforce(self):
        return UnboundedKnapshack.__recurse__(self.weights, self.profits, self.capacity, 0)

    @staticmethod
    def __recurse__(weights: List[int], profits: List[int], capacity: int, current: int):
        if current >= len(weights):
            return 0

        if capacity <= 0:
            return 0

        profit_with_current = 0
        if weights[current] <= capacity:
            profit_with_current = profits[current] \
                                  + UnboundedKnapshack.__recurse__(weights, profits, capacity - weights[current], current)

        profit_without_current = UnboundedKnapshack.__recurse__(weights, profits, capacity, current + 1)
        return max(profit_with_current, profit_without_current)

    def topdown(self):
        memo = [[-1 for _ in range(1 + self.capacity)] for _ in range(len(self.weights))]
        return UnboundedKnapshack.__recurse_memo__(self.weights, self.profits, self.capacity, 0, memo)

    @staticmethod
    def __recurse_memo__(weights: List[int], profits: List[int], capacity: int, current: int, memo: List[List[int]]):
        if current >= len(weights):
            return 0

        if capacity <= 0:
            return 0

        if memo[current][capacity] != -1:
            return memo[current][capacity]

        profit_with_current = 0
        if weights[current] <= capacity:
            profit_with_current = profits[current] \
                                  + UnboundedKnapshack.__recurse_memo__(weights, profits,
                                                                        capacity - weights[current], current, memo)

        profit_without_current = UnboundedKnapshack.__recurse_memo__(weights, profits, capacity, current + 1, memo)
        memo[current][capacity] = max(profit_with_current, profit_without_current)
        # print(memo)
        return memo[current][capacity]

    def bottomup(self):
        table = [[0 for _ in range(1 + self.capacity)] for _ in range(len(self.weights))]

        for cw in range(len(self.weights)):
            for cap in range(1, self.capacity + 1):
                profit_with_current = 0
                profit_without_current = 0

                if self.weights[cw] <= cap:
                    profit_with_current = self.profits[cw] + table[cw][cap - self.weights[cw]]
                if cw > 0:
                    profit_without_current = table[cw - 1][cap]

                table[cw][cap] = max(profit_with_current, profit_without_current)

        # print(table)
        return table[-1][self.capacity]


if __name__ == '__main__':
    w = [1, 3, 4, 5]
    p = [15, 50, 60, 90]
    c = 8
    UnboundedKnapshack(w, p, c).all_result()
