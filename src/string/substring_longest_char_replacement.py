#
# 424. Longest Repeating Character Replacement
# https://leetcode.com/problems/longest-repeating-character-replacement/description/
#
from collections import defaultdict


def char_replacement(s: str, k: int) -> int:
    """This is equivalent to find the substring with 'k' different chars.

    1) Hashmap, Two-Pointer:
    iterate through the string, use a Hashmap to count the chars

    at each step, count the possible max length of same chars
    check if the length of substring minus that is greater than k
    move the left side up accordingly

    as we are rolling check max at each step, the new possible
    max length of same chars that haven't been checked would be from
    the latest char added into the sequence

    time complexity: O(N), space complexity: O(C)
    """
    count: dict[str, int] = defaultdict(int)
    res, left, same_char_max = 0, 0, 0

    for right in range(len(s)):
        count[s[right]] += 1
        same_char_max = max(same_char_max, count[s[right]])

        # the left would always be <= k+1, so rolling move it once
        if (right - left + 1) - same_char_max > k:
            count[s[left]] -= 1
            left += 1

        res = max(res, right - left + 1)

    return res
