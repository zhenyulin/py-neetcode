#
# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/
#


def longest_palindrome(s: str) -> str:
    """Find the longest palindromic substring.

    1) Greedy Two-Pointer:
    iterate through 's', the minimum palindrome would be
        's[i]' and possibly 's[i:i+2]'
    for every 'i', use these two as the bases for exploration
    expand to both ends until 's[a:b]' is not palindrome
    compare and update output 's[l:r]' with the longest at each 'i'

    time complexity: O(n^2), space complexity: O(1)
    """
    l, r, n = 0, 1, len(s)

    for i in range(n):
        for a, b in (i - 1, i + 1), (i, i + 1):  # the possible palindrome bases
            while a >= 0 and b < n and s[a] == s[b]:  # expand both ends until it is not a palindrome
                a, b = a - 1, b + 1  # noqa: PLW2901 - legit overwrite without side effects

            if b - (a + 1) > r - l:  # s[a+1:b] is the possible longest palindrome at i
                l, r = a + 1, b

    return s[l:r]
