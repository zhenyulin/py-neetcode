#
# 1143. Longest Common Subsequence
# https://leetcode.com/problems/longest-common-subsequence/
#


def longest_common_subsequence(text1: str, text2: str) -> int:
    """For subsequence, it is common to use dynamic programming, for 2 strings we can.

    1) 2D Dynamic Programming

    dp[i][j] denotes the longest common subsequence between text1[:i] and text2[:j]

    relate condition for dp[i][j] is text1[i-1] == text2[j-1]
    else would be the same as i-1 or j-1 in one of the strings
    """
    # m, n = len(text1), len(text2)

    # dp = [[0] * (n + 1) for _ in range(m + 1)]

    # for i in range(1, m + 1):
    #     for j in range(1, n + 1):
    #         dp[i][j] = (
    #             dp[i - 1][j - 1] + 1 if text1[i - 1] == text2[j - 1] else max(dp[i - 1][j], dp[i][j - 1])
    #         )

    # return dp[m][n]
    """
    2) Memory Optimised 2D Dynamic Programming (1D)

    use a variable to denote the dp[i] as it iterates through text1
    use dp[j+1] to denote the longest subsequence at text2[j] updated at each i

    time complexity: O(m*n), space complexity: O(m*n)
    """
    n = len(text2)
    dp = [0] * (n + 1)

    for a in text1:
        i_max = 0
        for j, b in enumerate(text2):
            i_max_next = dp[j + 1]  # equivalent to dp[i][j+1], for s1[:i], s2[:j+1]
            # updating dp[i+1][j+1]
            # when a != b, drop either s1[i] or s2[j], i.e. dp[i-1][j] or dp[i][j-1] -> dp[j+1] or dp[j]
            dp[j + 1] = i_max + 1 if a == b else max(dp[j + 1], dp[j])
            i_max = i_max_next

    return dp[-1]
