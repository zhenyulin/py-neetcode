#
# 322. Coin Change
# https://leetcode.com/problems/coin-change/
#

from functools import cache


def fewest_elements_sum(coins: list[int], amount: int) -> int:
    """fn(amount) can be related to fn(amount - coin).

    1) Dynamic Programming
    dp[a] = min(dp[a], dp[a-c] + 1) if a coin can be used

    time complexity: O(A*C), space complexity: O(A)

    2) Cached DFS
    breaking down the large amount into smaller cached amount

    *saved time and space for dp[a] not used later

    time complexity: O(LogA?*C), space complexity: O(A)
    """
    # dp = [0] + [float("inf")] * amount

    # for a in range(1, amount + 1):
    #     for c in coins:
    #         if c <= a:
    #             dp[a] = min(dp[a], 1 + dp[a - c])

    # return dp[amount] if dp[amount] < float("inf") else -1

    @cache
    def fn(n):
        if n == 0:
            return 0
        elif n < 0:
            return float("inf")

        return min(1 + fn(n - coin) for coin in coins)

    return fn(amount) if fn(amount) < float("inf") else -1
