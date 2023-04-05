#
# 424. Longest Repeating Character Replacement
# https://leetcode.com/problems/longest-repeating-character-replacement/description/
#
from collections import defaultdict


def charReplacement(s: str, k: int) -> int:
    """
    this is equivalent to find the substring with 'k' different chars

    1) Hashmap:
    iterate through the string, use a Hashmap to count the chars

    at each step, count the possible max length of same chars
    check if the length of substring minus that is greater than k
    move the left side up accordingly

    as we are rolling check max at each step, the new possible
    max length of same chars that haven't been checked would be from
    the latest char added into the sequence

    time complexity: O(N), space complexity: O(C)
    """
    count, res, l, same_char_max = defaultdict(int), 0, 0, 0

    for r in range(len(s)):
        count[s[r]] += 1
        same_char_max = max(same_char_max, count[s[r]])

        if (r + 1 - l) - same_char_max > k:
            count[s[l]] -= 1
            l += 1

        res = max(res, r + 1 - l)

    return res
