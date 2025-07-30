#
# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
#
from collections import defaultdict


def length_of_longest_substring(s: str) -> int:
    """Find the longest substring without repeating characters.

    1) Hashmap, Two-Pointer:
    we can iterate through the string with two pointers s[i:j] to denote a substring
    that contains only unique characters.

    along the way, we can use a hashmap to store the last index of each character
    when the new character from iterator is found in the hashmap
    we update i according to the last index of that character

    time complexity: O(N), space complexity: O(1)
    """
    seen: dict[str, int] = defaultdict(lambda: -1)
    res, i = 0, 0

    for j, c in enumerate(s):
        if seen[c] >= i:
            i = seen[c] + 1
        else:
            res = max(res, j - i + 1)

        seen[c] = j

    return res
