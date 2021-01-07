from dynamic import Dynamic


class Staircase(Dynamic):
    def __init__(self, stair: int):
        self.stair = stair

    def bruteforce(self):
        return self.__recurse__(self.stair)

    def __recurse__(self, n: int):
        if n == 0:
            return 1

        if n == 1:
            return 1

        if n == 2:
            return 2

        return self.__recurse__(n - 3) + self.__recurse__(n - 2) + self.__recurse__(n - 1)

    def topdown(self):
        memo = [-1 for i in range(0, self.stair + 1)]
        memo[0] = 1
        memo[1] = 1
        memo[2] = 2
        return self.__recurse_memo__(self.stair, memo)

    def __recurse_memo__(self, n: int, memo):
        if memo[n] > 0:
            return memo[n]

        memo[n] = self.__recurse_memo__(n - 1, memo) \
                  + self.__recurse_memo__(n - 2, memo) \
                  + self.__recurse_memo__(n - 3, memo)
        return memo[n]

    def bottomup(self):
        table = [-1 for i in range(0, self.stair + 1)]
        table[0] = 1
        table[1] = 1
        table[2] = 2
        for n in range(3, self.stair + 1):
            table[n] = table[n - 1] + table[n - 2] + table[n - 3]

        return table[self.stair]


if __name__ == '__main__':
    staircase = Staircase(5)
    staircase.all_result()
