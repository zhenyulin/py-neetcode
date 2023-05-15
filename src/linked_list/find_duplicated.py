#
# 287. Find the Duplicate Numbe
# https://leetcode.com/problems/find-the-duplicate-number/
#


def findDuplicate(nums: list[int]) -> int:
    res = fast = slow = 0

    while fast != slow or slow == 0:
        slow = nums[slow]
        fast = nums[nums[fast]]

    while res != slow:
        res = nums[res]
        slow = nums[slow]

    return res
