#
# 15. 3Sum
# https://leetcode.com/problems/3sum/


def three_sum(nums: list[int]) -> list[list[int]]:
    """Sort + two-pointer.

    time complexity: O(N^2), space complexity: O(1)
    """
    nums.sort()
    n = len(nums)
    res = []

    for i in range(n - 2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, n - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s == 0:
                res.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1
            elif s < 0:
                l += 1
            else:
                r -= 1

    return res
