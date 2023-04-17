#
# 29. Divide Two Integers
# https://leetcode.com/problems/divide-two-integers/
#


def divide(dividend: int, divisor: int) -> int:
    """
    we can use deduction for division without multiplication, division and mod

    1) Bit Shift, Greedy

    to speed up the process, we can amplify the divisor by bit shift (<< 1 ~ * 2)

    time complexity: O(LogN), space complexity: O(1)

    * N = dividend // divisor
    """

    a, b = abs(dividend), abs(divisor)

    res = 0

    while a >= b:

        _b, k = b, 1

        while a >= _b:

            a -= _b
            res += k

            _b, k = _b << 1, k << 1

    if (dividend > 0) ^ (divisor > 0):
        res *= -1

    return min(max(-(2**31), res), 2**31 - 1)
