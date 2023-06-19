#
# 268. Missing Number
# https://leetcode.com/problems/missing-number/
#


def missingNumber(nums: list[int]) -> int:
    """
    to find the missing number between [0, n] from nums of length n

    1) Greedy

    the missing number is simply the diff of sums of [1, n] and nums

    time complexity: O(N), space complexity: O(1)
    """

    diff = 0

    for i, n in enumerate(nums):
        diff += i + 1 - n

    return diff
