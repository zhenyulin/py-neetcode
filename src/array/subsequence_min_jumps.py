#
# 45. Jump Game II
# https://leetcode.com/problems/jump-game-ii/
#


def min_jump(nums: list[int]) -> int:
    """1) Dynamic Programming.

    dp[r+1] = min(dp[i] + 1 if nums[l] >= r + 1 - l for i in range(l, r+1))

    time complexity: O(N), space complexity: O(N)

    2) Implicit BFS

    iterate from the left, at each step check the furthest each cell can reach
    step up only if it passes the previous furthest or it has reached the end
    (reached the furthest for the current step)

    time complexity: O(N), space complexity: O(1)
    """
    res, start, end = 0, 0, 0

    # last cell is to be reached
    while end < len(nums) - 1:
        # as it is guaranteed to reach last cell
        # end is always >= start (last furthest >= end + 1)
        furthest = start
        for i in range(start, end + 1):
            furthest = max(furthest, i + nums[i])
        start = end + 1
        end = furthest
        res += 1

    return res
