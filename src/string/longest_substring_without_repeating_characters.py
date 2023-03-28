#
# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
#


def lengthOfLongestSubstring(s: str) -> int:
    """find the longest substring without repeating characters

    1) Hashmap:
    we can use a Hashmap to record the index of last seen `char` iterating `s`
    and use `i` to denote the index where all chars have only appeared once

    `i` will be updated every time we find a `seen[c]` no less than i
    so that we can ensure no char in `s[i: j+1]` has been seen before

    time complexity: O(N), memory complexity: O(1)
    """

    res, i, seen = 0, 0, {}

    for j, c in enumerate(s):
        if c in seen and seen[c] >= i:
            i = seen[c] + 1
        else:
            res = max(res, j + 1 - i)

        seen[c] = j

    return res
