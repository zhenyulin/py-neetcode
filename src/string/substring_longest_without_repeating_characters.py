#
# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
#


def lengthOfLongestSubstring(s: str) -> int:
    """Find the longest substring without repeating characters.

    1) Hashmap:
    we can use a Hashmap to record the index of 'c' last seen iterating 's'
    and use 'i' to denote the index where no char in s[i:j+1] has been seen

    'i' will be updated every time we find a 'seen[c]' no less than i

    * this will make 'i > max[seen[c] for c in s[i:j+1] if c in seen]'

    time complexity: O(N), space complexity: O(1)
    """
    res, i, seen = 0, 0, {}

    for j, c in enumerate(s):
        if c in seen and seen[c] >= i:
            i = seen[c] + 1
        else:
            res = max(res, j + 1 - i)

        seen[c] = j

    return res
