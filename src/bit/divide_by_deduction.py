#
# 29. Divide Two Integers
# https://leetcode.com/problems/divide-two-integers/
#


def divide(dividend: int, divisor: int) -> int:
    """We can use deduction for division without multiplication, division and mod.

    1) Bit Shift

    to speed up the process, we can amplify the divisor by bit shift (<< 1 ~ * 2)
    and since the dividend is capped within a byte, we can try from 31 shifts to 0

    time complexity: O(1), space complexity: O(1)
    """
    a, b, res, CAP = abs(dividend), abs(divisor), 0, 2**31

    for power in range(31, -1, -1):
        if (b << power) <= a:
            res += 1 << power
            a -= b << power

    if (dividend > 0) != (divisor > 0):
        res *= -1

    return min(max(-CAP, res), CAP - 1)
