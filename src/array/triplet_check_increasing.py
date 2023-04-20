#
# 334. Increasing Triplet Subsequence
# https://leetcode.com/problems/increasing-triplet-subsequence/
#


def increasingTriplet(nums: list[int]) -> bool:
    """
    1) Greedy

    can be turned into a finding larger num during iteration with anchors

    time complexity: O(N), space complexity: O(1)
    """

    a = b = float("inf")

    for n in nums:
        if n <= a:
            a = n
        elif n <= b:
            b = n
        else:
            return True

    return False
