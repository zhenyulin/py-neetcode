#
# 239. Sliding Window Maximum
# https://leetcode.com/problems/sliding-window-maximum/
#
from collections import deque


def windowMaxes(nums: list[int], k: int) -> list[int]:
    """
    to record the maxes of window sliding

    we need to find an effciient data structure to record the max
    and rolling update it with shifting indexes

    1) Monotonic Stack

    we use a stack to record the index 'i' of the max num until 'i'
    and rolling update the index, append it to the result before it expires

    time complexity: O(N), space complexity: O(K)
    """

    stack, res = deque(), []

    for i, n in enumerate(nums):

        # keep only the index of the max number until 'i'
        while stack and nums[stack[-1]] < n:
            stack.pop()

        stack.append(i)

        # range of index should < k, remove the index when it expires
        if i - stack[0] == k:
            stack.popleft()

        # start to append result when i reaches window size
        if i >= k - 1:
            res.append(nums[stack[0]])

    return res
