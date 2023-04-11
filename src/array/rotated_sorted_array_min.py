#
# 153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
#


def findMin(nums: list[int]) -> int:
    """

    the array after rotation will have 2 incremental parts (or like original)

    1) Binary Search
    in a sorted array, even rotated, by binary searching the smaller part
    i.e. update the higher bound(right), we will converge to the minimal

    time complexity: O(LogN), space complexity: O(1)
    """

    left, right = 0, len(nums) - 1

    while left < right:
        m = (left + right) // 2

        # target condition is middle point being smaller than the right
        if nums[m] < nums[right]:
            right = m
        else:
            left = m + 1

    return nums[left]
