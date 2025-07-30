#
# 1573. number of Ways to Split a String
# https://leetcode.com/problems/number-of-ways-to-split-a-string/
#

MOD_BASE = 10**9 + 7


def num_ways(s: str) -> int:
    """To count ways to split the string with equal amount of 1.

    we just need to record the indexes of n/3 and 2*n/3 for 1

    1) Math, Greedy:

    time complexity: O(n), space complexity: O(1)
    """
    ones = s.count("1")

    if ones == 0:
        return (len(s) - 1) * (len(s) - 2) // 2 % MOD_BASE

    if ones % 3:
        return 0

    first, second, count = 0, 0, 0

    for char in s:
        if char == "1":
            count += 1

        if count == ones // 3:
            first += 1
        elif count == 2 * ones // 3:
            second += 1
        elif count > 2 * ones // 3:
            break

    return first * second % MOD_BASE
