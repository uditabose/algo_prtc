from dynamic import Dynamic


class CoinChange(Dynamic):
    def __init__(self, denomination, total):
        self.denomination = denomination
        self.total = total

    def bruteforce(self):
        return CoinChange.__recurse__(self.denomination, self.total, 0)

    @staticmethod
    def __recurse__(denomination, total, current):
        if total == 0:
            return 1

        dn = len(denomination)
        if current >= dn:
            return 0

        change_with_current = 0
        if total >= denomination[current]:
            change_with_current = CoinChange.__recurse__(denomination, total - denomination[current], current)

        change_without_current = CoinChange.__recurse__(denomination, total, current + 1)

        return change_with_current + change_without_current

    def topdown(self):
        memo = [[-1 for _ in range(self.total + 1)] for _ in range(len(self.denomination))]
        return CoinChange.__recurse_memo__(self.denomination, self.total, 0, memo)

    @staticmethod
    def __recurse_memo__(denomination, total, current, memo):
        if total == 0:
            return 1

        dn = len(denomination)
        if current >= dn:
            return 0

        if memo[current][total] != -1:
            return memo[current][total]

        change_with_current = 0
        if total >= denomination[current]:
            change_with_current = CoinChange.__recurse_memo__(denomination, total - denomination[current], current, memo)

        change_without_current = CoinChange.__recurse_memo__(denomination, total, current + 1, memo)

        memo[current][total] = change_with_current + change_without_current
        # print(memo)
        return memo[current][total]

    def bottomup(self):
        dn = len(self.denomination)
        table = [[0 for _ in range(self.total + 1)] for _ in range(dn)]
        for i in range(dn):
            table[i][0] = 1

        for denom in range(dn):
            for tot in range(1, self.total + 1):
                if denom > 0:
                    table[denom][tot] = table[denom - 1][tot]

                if self.denomination[denom] <= tot:
                    table[denom][tot] += table[denom][tot - self.denomination[denom]]

        # print(table)
        return table[-1][self.total]


if __name__ == '__main__':
    d = [1, 2, 3]
    t = 5
    CoinChange(d, t).all_result()
