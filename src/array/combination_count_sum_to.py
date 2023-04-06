#
# 518. Coin Change II
# https://leetcode.com/problems/coin-change-ii/
#


def waysOfChange(coins: list[int], amount: int) -> int:
    """
    fn(amount) is related to various fn(amount - coin), therefore dynamic programming

    1) Dynamic Programming
    dp[i] denotes the ways of change for amount i

    dp[i] += dp[i-coin]
    """

    dp = [1] + [0] * amount

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]
