#
# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/
#


def longestPalindrome(s: str) -> str:
    """Find the longest palindromic substring.

    1) Greedy:
    iterate through 's', the minimum palindrome would be
        's[i]' and possibly 's[i:i+2]'
    for every 'i', use these two as the bases for exploration
    expand to both ends until 's[a:b]' is not palindrome
    compare and update output 's[l:r]' with the longest at each 'i'

    time complexity: O(N^2), space complexity: O(1)

    X) Dynamic Programming:
    for a palindrome, the centre is critical,
    'dp[i]' may not be directly related to 'dp[i-1]'
    whether using 'dp[i]' to denote the longest palindromic substring in s[:i]
    or centred at s[i]
    """
    l, r, N = 0, 1, len(s)

    for i in range(N):
        # the possible palindrome bases
        for a, b in (i, i), (i, i + 1):
            # expand both ends until it is not a palindrome
            while 0 <= a and b < N and s[a] == s[b]:
                a, b = a - 1, b + 1

            if b - a - 1 > r - l:
                # s[a+1:b] is the possible longest palindrome at i
                l, r = a + 1, b

    return s[l:r]
