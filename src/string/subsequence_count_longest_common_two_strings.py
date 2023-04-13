#
# 1143. Longest Common Subsequence
# https://leetcode.com/problems/longest-common-subsequence/
#


def longestCommonSubsequence(text1: str, text2: str) -> int:
    """
    for subsequence, it is common to use dynamic programming, for 2 strings we can

    1) 2D Dynamic Programming

    dp[i][j] denotes the longest common subsequence between text1[:i] and text2[:j]

    relate conditon for dp[i][j] is text1[i-1] == text2[j-1]
    else would be the same as i-1 or j-1 in one of the strings

    time complexity: O(M*N), space complexity: O(M*N)
    """
    M, N = len(text1), len(text2)

    dp = [[0] * (N + 1) for _ in range(M + 1)]

    for i in range(1, M + 1):
        for j in range(1, N + 1):
            dp[i][j] = (
                dp[i - 1][j - 1] + 1
                if text1[i - 1] == text2[j - 1]
                else max(dp[i - 1][j], dp[i][j - 1])
            )

    return dp[M][N]
