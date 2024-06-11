#
# 547. Number of Provinces
# https://leetcode.com/problems/number-of-provinces/description/
#
from collections import defaultdict


def countGroups(connections: list[list[int]]) -> int:
    """To count unique groups, we can use DFS
    we can also form a graph to reduce repeated searching.

    1) DFS

    time complexity: O(N^2), space complexity: O(N+2*M)
    * M is the average connections in the graph
    """
    if not connections:
        return 0

    graph = defaultdict(list)

    for i in range(len(connections)):
        for j in range(i + 1, len(connections)):
            if connections[i][j]:
                graph[i].append(j)
                graph[j].append(i)

    visited = [False] * len(connections)

    def dfs(i):
        for j in graph[i]:
            # { search condition }
            if not visited[j]:
                visited[j] = True
                dfs(j)

    res = 0
    for i in range(len(connections)):
        if not visited[i]:
            res += 1
            visited[i] = True
            dfs(i)

    return res
