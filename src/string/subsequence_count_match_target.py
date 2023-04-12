#
# 115. Distinct Subsequences
# https://leetcode.com/problems/distinct-subsequences/
#


def numMatchSubsequences(s: str, t: str) -> int:
    """to count the number of unique subsequences matching the target

    1) 2D Dynamic Programming

    for t[:j], s[:i] can always sample from s[:i-1]
    and if s[i-1] == t[j-1], then those two chars can be removed
    the ways sampling in s[:i-1] for t[:j-1] can also be used

    time complexity: O(M*N), space complexity: O(M*N)
    """

    # dp = [[1] + [0] * len(t) for _ in range(len(s) + 1)]

    # for i, a in enumerate(s):
    #     for j, b in enumerate(t):
    #         # dp[i][j] denotes the unique subsequence count for s[:i] and t[:j]
    #         # dp[i][j] will be related to dp[i-1][j-1] and dp[i-1][j]
    #         # depending on if s[i-1] == t[j-1]
    #         dp[i + 1][j + 1] = dp[i][j + 1] + (dp[i][j] if a == b else 0)

    # return dp[-1][-1]

    """2) simplified 2D Dynamic Programming

    iterate through s
    using an array to record ways of how s[:i] can match substrings of target

    time complexity: O(M*N), space complexity: O(N)
    """

    match = [1] + [0] * len(t)

    for i in range(len(s)):
        current = [1]

        for j in range(len(t)):
            current.append(match[j + 1] + (match[j] if s[i] == t[j] else 0))

        match = current

    return match[-1]
