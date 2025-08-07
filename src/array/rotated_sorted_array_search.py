#
# 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/
#


def search(nums: list[int], target: int) -> int:
    """To search target in a rotated incremental array.

    This is equivalent to two incremental arrays, at each Binary Search could be applied.
    So we just need to add a mid-point condition to confirm whether we are in the incremental.

    1) Binary Search
    find the sorted part of the array covering the target first
    update the boundary to converge to the target

    time complexity: O(LogN), space complexity: O(1)
    """
    l, r = 0, len(nums) - 1

    while l <= r:
        m = (l + r) // 2

        if target == nums[m]:
            return m

        # sorted part is on the left
        if nums[l] < nums[m]:
            # target in the sorted part, just close the boundary
            if nums[l] <= target < nums[m]:
                r = m - 1
            # not in the sorted part, check the other part
            else:
                l = m + 1
        # sorted part is on the right, act accordingly
        elif nums[m] < target <= nums[r]:
            l = m + 1
        else:
            r = m - 1

    return -1
