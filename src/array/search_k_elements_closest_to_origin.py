#
# 973. K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/
#
from heapq import heappop, heappush


def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    """Find kth closest point, we can calculate the Euclidean distance, and use.

    1) Heap

    time complexity: O(K*LogN), space complexity: O(N)
    """
    distances: list[list[int]] = []
    for x, y in points:
        d = abs(x) ** 2 + abs(y) ** 2
        heappush(distances, [d, x, y])

    res: list[list[int]] = []
    for _ in range(k):
        d, x, y = heappop(distances)
        res.append([x, y])

    return res
