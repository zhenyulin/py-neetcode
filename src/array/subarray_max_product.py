#
# 152. Maximum Product Subarray
# https://leetcode.com/problems/maximum-product-subarray/
#


def maxProduct(nums: list[int]) -> int:
    """For product, the absolute value won't decrease timing a new int except 0.

    1) Greedy:
    record both the min, max for the max absolute values in both signs
    update max, min candidates at each step, rolling update res
    """
    res = _max = _min = nums[0]

    for n in nums[1:]:
        # include n in case _max, _min where last reset to 0
        vals = (n, n * _max, n * _min)
        _max, _min = max(vals), min(vals)
        res = max(res, _max)

    return res
