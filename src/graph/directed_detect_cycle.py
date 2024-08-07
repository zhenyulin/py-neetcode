#
# 207. Course Schedule
# https://leetcode.com/problems/course-schedule/description/
#
from collections import defaultdict, deque


def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    """Check if there's cycle in a directed graph.

    1) Topological Sort

    we can taking off the nodes of no dependencies, reduce the depedency count
    and again

    graph: {up: [downs]}

    time complexity: O(C), space complexity: O(C+N)
    * C is the number of connections, length of prerequisites
    * N is the number of nodes (courses)
    """
    downs, up_counts = defaultdict(list), [0] * numCourses

    for c, p in prerequisites:
        downs[p].append(c)
        up_counts[c] += 1

    solvables = deque([i for i, count in enumerate(up_counts) if count == 0])

    solvable_count = 0
    while solvables:
        u = solvables.popleft()
        solvable_count += 1

        for d in downs[u]:
            up_counts[d] -= 1
            if up_counts[d] == 0:
                solvables.append(d)

    return solvable_count == numCourses
