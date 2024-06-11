#
# 209. Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/
#


def minSubArrayLen(target: int, nums: list[int]) -> int:
    """1) Greedy (left, right sliding window).

    time complexity: O(N), space complexity: O(1)
    """
    i, j, s, res = 0, 0, 0, len(nums) + 1

    while j < len(nums):

        s += nums[j]

        while s >= target:
            res = min(res, j - i + 1)
            s -= nums[i]
            i += 1
        else:
            j += 1

    return 0 if res > len(nums) else res
