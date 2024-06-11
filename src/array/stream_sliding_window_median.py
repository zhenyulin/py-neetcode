#
# 480. Sliding Window Median
# https://leetcode.com/problems/sliding-window-median/description/
#
from collections import defaultdict
from heapq import heappop, heappush, heappushpop


def slidingWindowMedian(nums: list[int], k: int) -> list[float]:
    """We can use min-max heaps for median value.

    see [295. Find Median from Data Stream]
    (./stream_find_median_element.py)

    0) Iterate, Sort, Remove

    time complexity: O((N-K)*K*LogK), space complexity: O(K)

    1) Max-Min Heap, Lazy Removal

    time complexity: O(N*Log(K)), space complexity: O(N)
    """
    res, left, right, expires = [], [], [], defaultdict(int)

    for i in range(len(nums)):

        heappush(left, -heappushpop(right, nums[i]))

        # prefer right heap
        # when not all elements are within the window
        # using only the lazy removal rule of expires to move left to right
        if i < k and len(left) > len(right):
            heappush(right, -heappop(left))

        # lazy removal
        if i >= k:
            expired = nums[i - k]
            expires[expired] += 1

            # if the expired is on the left and not left[0]
            # then it doesn't affect the median
            # elif it is on the right
            # then 1 element on the right potentially needs to be removed,
            # therefore the right needs to be filled from the left by one
            if expired > -left[0]:
                heappush(right, -heappop(left))
            while left and expires.get(-left[0]):
                expires[-left[0]] -= 1
                heappop(left)
            while right and expires.get(right[0]):
                expires[right[0]] -= 1
                heappop(right)

        if i >= k - 1:
            res.append(float(right[0]) if k % 2 else (right[0] - left[0]) / 2)

    return res
