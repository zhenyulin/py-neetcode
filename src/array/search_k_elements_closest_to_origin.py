#
# 973. K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/
#
from typing import Tuple
from heapq import heappush, heappop


def kClosest(points: list[list[int]], k: int) -> list[Tuple[int, int]]:
    """
    find kth closest point, we can calculate the Euclidean distance, and use

    1) Heap

    time complexity: O(N), space complexity: O(N)
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
