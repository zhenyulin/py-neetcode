"""
Given an array arr[] consisting of N integers,
the task is to find the maximum sum of any subsequence
from the array having Bitwise AND of its elements
not equal to zero.
"""


def maxSum(nums: list[int]) -> int:
    """to find the max sum of elements whose bitwise AND isn't zero

    then those elements should all be 1 on at least one common bit

    1) Bit Iteration

    time complexity: O(1), space complexity: O(1)
    """

    res, bit = 0, 1
    # check the max sum on each common bit
    for _ in range(32):
        elements = [n for n in nums if n & bit]
        res = max(res, sum(elements))
        bit = bit << 1

    return res
