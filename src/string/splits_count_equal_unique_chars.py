#
# 1525. Number of Good Ways to Split a String
# https://leetcode.com/problems/number-of-good-ways-to-split-a-string/
#


def num_split(s: str) -> int:
    """To count unique chars on both end.

    we can use a hashmap to record 'first' and 'last' appearance of a char
    then for each index i we know how many unique chars are before and after
    Note: set wouldn't work for removing char

    to have equal amount of unique chars, the index i will need to be
    between a scope where there're equal amount of 'last' before and 'first' after

    to find this, we can merge 'first' and 'last', sort it and find the mid point

    time complexity: O(N), space complexity: O(C)
    """
    first, last = {}, {}

    for i, c in enumerate(s):
        if c not in first:
            first[c] = i
        last[c] = i

    ranges = sorted([*first.values(), *last.values()])

    mid = len(ranges) // 2

    return ranges[mid] - ranges[mid - 1]
