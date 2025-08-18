#
# 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/
#


def longest_consecutive_sequence(nums: list[int]) -> int:
    """Return the length of the longest consecutive number sequence.

    1) Greedy:

    iterate through 'nums', for each 'n'
    increase 'length' until 'n+length' is not in 'set(nums)'

    time complexity: O(N), space complexity: O(N)
    """
    res, _nums = 0, set(nums)

    for n in _nums:
        # don't check if it has been checked as an intermediate point
        if n - 1 not in _nums:
            m = 1
            while n + m in _nums:
                m += 1
            res = max(res, m)

    return res
