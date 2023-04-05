#
# 300. Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/
#


def longestIncreasingSubsequence(nums: list[int]) -> int:
    """
    dp[j] is related to dp[i] if nums[j] > nums[i]

    1) Dynamic Programming

    time complexity: O(N^2), space complexity: O(N)
    """

    dp = [1] * len(nums)

    for j in range(len(nums)):
        dp[j] = max([1] + [dp[i] + 1 for i in range(j) if nums[j] > nums[i]])

    return max(dp)
