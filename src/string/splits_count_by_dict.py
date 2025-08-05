#
# 91. Decode Ways
# https://leetcode.com/problems/decode-ways/
#


def ways_of_decoding(s: str) -> int:
    """n-2, n-1 are incrementally related to n, with dual ways at each step.

    1) Dynamic Programming

    time complexity: O(N), space complexity: O(1)
    """
    if s[0] == "0":
        return 0

    prev, current = 1, 1

    for i in range(1, len(s)):
        _next = 0

        if s[i] != "0":
            _next += current
        if "10" <= s[i - 1 : i + 1] <= "26":
            _next += prev

        prev, current = current, _next

    return current
