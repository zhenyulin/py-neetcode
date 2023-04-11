#
# 162. Find Peak Element
# https://leetcode.com/problems/find-peak-element/
#


def findPeakElement(nums: list[int]) -> int:
    """find the index to the any of the peaks

    1) Binary Search

    there can be multiple peaks with uphills and downhills

    if the searching point is on uphill, we will look for target on the right
    so that left is always on uphill or peak (by `left = m + 1`)
    if it is on downhill, then we move the right to mid (`right = m`)
    so that right is always on downhill or peak
    and finally they would converge to peak

    time complexity: O(LogN), space complexity: O(1)
    """

    left, right = 0, len(nums) - 1

    while left < right:
        m = (left + right) // 2

        # { target conditoin } - mid element larger than next
        if nums[m] > nums[m + 1]:
            right = m  # m could be peak point already
        else:
            left = m + 1

    # when left converges to right, and nums[m] is peak
    return left
