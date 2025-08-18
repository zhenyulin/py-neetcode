#
# 910. Smallest Range II
# https://leetcode.com/problems/smallest-range-ii/
#
import itertools


def smallest_range(nums: list[int], k: int) -> int:
    """We need to find the possible closest new min and new max to reduce the gap.

    after sorting the array, the maximum value after operation is either m - k or a + k
    and the minimum value candidates are either n + k or b - k
    so we can iterate through the array record the min of the gap between the max and min.

    1) Greedy

    we can init with res as 'm - n' with non-update operations
    find the possible candidates, rolling update res

    time complexity: O(N), space complexity: O(1)
    """
    nums.sort()

    n, m = nums[0], nums[-1]
    res = m - n

    for a, b in itertools.pairwise(nums):
        res = min(res, max(m - k, a + k) - min(n + k, b - k))

    return res
