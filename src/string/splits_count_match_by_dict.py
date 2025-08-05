#
# 139. Word Break
# https://leetcode.com/problems/word-break/
#


def word_break(s: str, words: list[str]) -> bool:
    """Whether s is breakable would be related to s[i-len(w)] is breakable.

    1) Dynamic Programming

    time complexity: O(S*W), space complexity: O(S)
    """
    # dp[i] denotes if s[:i] is breakable
    dp = [True] + [False] * len(s)

    for i in range(1, len(s) + 1):
        dp[i] = any(True for w in words if dp[i - len(w)] and s[i - len(w) : i] == w)

    return dp[-1]
