#
# 973. K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/
#
from heapq import heappop, heappush
from typing import Tuple


def kClosest(points: list[list[int]], k: int) -> list[Tuple[int, int]]:
    """Find kth closest point, we can calculate the Euclidean distance, and use.

    1) Heap

    time complexity: O(K*LogN), space complexity: O(N)
    """
    distances = []
    for x, y in points:
        d = abs(x) ** 2 + abs(y) ** 2
        heappush(distances, [d, x, y])

    res = []
    for _ in range(k):
        d, x, y = heappop(distances)
        res.append([x, y])

    return res
