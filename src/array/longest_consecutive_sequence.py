#
# 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/
#


def longestConsecutiveSequence(nums: list[int]) -> int:
    """return the length of the longest consecutive number sequence

    1) Greedy:

    iterate through 'nums', for each 'n'
    increase 'length' until 'n+length' is not in 'set(nums)'

    time complexity: O(N), space complexity: O(N)
    """
    res, nums = 0, set(nums)

    for n in nums:
        # don't check if it has been checked as "n'+length"
        if n - 1 not in nums:
            length = 1
            while n + length in nums:
                length += 1
            res = max(res, length)

    return res
