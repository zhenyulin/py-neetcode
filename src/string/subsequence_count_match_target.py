#
# 115. Distinct Subsequences
# https://leetcode.com/problems/distinct-subsequences/
#


def num_match_subsequences(s: str, t: str) -> int:
    """To count the number of unique subsequences matching the target.

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
    # match[j+1] denote the match count to t[:j+1], use a leading 1 for initial match
    match = [1] + [0] * len(t)

    for c in s:
        # when a new matching char found, we can choose to drop the current match or previous match
        for j in range(len(t) - 1, -1, -1):
            match[j + 1] += match[j] if c == t[j] else 0

    return match[-1]
