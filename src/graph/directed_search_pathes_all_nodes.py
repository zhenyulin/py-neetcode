#
# 210. Course Schedule II
# https://leetcode.com/problems/course-schedule-ii/
#
from collections import defaultdict, deque


def findPathes(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    """
    which means there are no cycles in the directed graph
    so we can use the same process

    1) Topological Sort

    time complexity: O(C), space complexity: O(C+N)
    * C is the number of connections, length of prerequisites
    * N is the number of nodes (courses)
    """

    downs, up_counts = defaultdict(list), [0] * numCourses

    for c, p in prerequisites:
        downs[p].append(c)
        up_counts[c] += 1

    independants = deque([i for i, count in enumerate(up_counts) if count == 0])

    res = []

    while independants:
        u = independants.popleft()
        res.append(u)

        for d in downs[u]:
            up_counts[d] -= 1
            if up_counts[d] == 0:
                independants.append(d)

    return res if len(res) == numCourses else []
