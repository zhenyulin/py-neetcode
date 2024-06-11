#
# 1073. Adding Two Negabinary Numbers
# https://leetcode.com/problems/adding-two-negabinary-numbers/
#


def addNegaBinary(arr1: list[int], arr2: list[int]) -> list[int]:
    """1) Calculation per Bit.

    in negative base, the values of bits alter between negative and positive
    so the carry will be negative to the next bit, so needs to be deducted not added
    the current bit can use the positive base

    time complexity: O(N), space complexity: O(N)
    """

    def safe_pop(arr):
        return arr.pop() if arr else 0

    res, carry = [], 0

    while arr1 or arr2 or carry:
        carry, bit = divmod(safe_pop(arr1) + safe_pop(arr2) - carry, 2)
        res.append(bit)

    # because carry is deducted, it can produce leading zeros
    while len(res) > 1 and res[-1] == 0:
        res.pop()

    return res[::-1]
