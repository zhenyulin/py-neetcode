#
# 1573. Number of Ways to Split a String
# https://leetcode.com/problems/number-of-ways-to-split-a-string/
#


def numWays(s: str) -> int:
    """To count ways to split the string with equal amount of 1.

    we just need to record the indexes of N/3 and 2*N/3 for 1

    1) Math, Greedy:

    time complexity: O(N), space complexity: O(1)
    """
    N, MOD_BASE = s.count("1"), 10**9 + 7

    if N == 0:
        return (len(s) - 1) * (len(s) - 2) // 2 % MOD_BASE

    if N % 3:
        return 0

    a, b, count = 0, 0, 0

    for c in s:

        if c == "1":
            count += 1

        if count == N // 3:
            a += 1
        elif count == 2 * N // 3:
            b += 1
        elif count > 2 * N // 3:
            break

    return a * b % MOD_BASE
