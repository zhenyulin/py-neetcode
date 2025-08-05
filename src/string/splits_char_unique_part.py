#
# 763. Partition Labels
# https://leetcode.com/problems/partition-labels/
#


def partition_lengths(s: str) -> list[int]:
    """1) Greedy, HashMap.

    to make sure unique char only appear in one part
    we can record the index of the char last appeared

    then we can then iterate through the string
    update the limit along the way to the limit,
    until i == limit, where no new limit (new char) encountered

    time complexity: O(N), space complexity: O(1)
    """
    last = {s[i]: i for i in range(len(s))}  # last appearance
    res, i, length, limit = [], 0, 0, 0

    while i < len(s):
        limit = max(limit, last[s[i]])
        length += 1

        # iterate until not encountering new char to limit
        if i == limit:
            res.append(length)
            length = 0

        i += 1

    return res
