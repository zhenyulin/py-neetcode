#
# 480. Sliding Window Median
# https://leetcode.com/problems/sliding-window-median/
#
from collections import defaultdict
from heapq import heappop, heappush, heappushpop


def sliding_window_median(nums: list[int], k: int) -> list[float]:
    """We can use min-max heaps for median value.

    see [295. Find Median from Data Stream]
    (./stream_find_median_element.py)

    0) Iterate, Sort, Remove

    time complexity: O((N-K)*K*LogK), space complexity: O(K)

    1) Max-Min Heap, Lazy Removal

    time complexity: O(N*Log(K)), space complexity: O(N)
    """
    res: list[float]
    left: list[int]  # negative max heap
    right: list[int]  # ascending min heap
    expired: defaultdict[int, int]
    res, left, right, expired = [], [], [], defaultdict(int)

    for i in range(len(nums)):
        # order the left and right heaps
        heappush(right, -heappushpop(left, -nums[i]))

        # balance the sizes, storing potential median at left
        if i < k and len(right) > len(left):
            heappush(left, -heappop(right))

        # lazy removal - only remove the expired when it is at the top of heaps
        # still need to balance the actual size of the heaps to ensure median in left
        if i >= k:
            expiring = nums[i - k]
            expired[expiring] += 1

            # if the expiring is in the left, move one from the right to balance the size
            # this needs to be done before the pruning, so that the boundary condition is valid
            if expiring <= -left[0]:
                heappush(left, -heappop(right))

            # prune the expired elements at the top of the heaps
            while left and expired.get(-left[0]):
                expired[-left[0]] -= 1
                heappop(left)
            while right and expired.get(right[0]):
                expired[right[0]] -= 1
                heappop(right)

        if i >= k - 1:
            res.append(float(-left[0]) if k % 2 else (right[0] - left[0]) / 2)

    return res
