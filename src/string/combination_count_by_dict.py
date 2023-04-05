#
# 91. Decode Ways
# https://leetcode.com/problems/decode-ways/
#


def waysOfDecoding(s: str) -> int:
    """
    n-2, n-1 are incrementally related to n, with two ways at each step

    1) Dynamic Programming

    time complexity: O(N), space complexity: O(1)
    """
    if s[0] == "0":
        return 0

    ONE = [str(i) for i in range(1, 10)]
    TWO = [str(i) for i in range(10, 27)]

    current, last, prev = 1, 1, 1

    for i in range(1, len(s)):

        current, last, prev = 0, current, last

        if s[i] in ONE:
            current += last
        if s[i - 1 : i + 1] in TWO:
            current += prev

    return current
