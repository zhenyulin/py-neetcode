#
# 684. Redundant Connection
# https://leetcode.com/problems/redundant-connection/
#


def removeCycle(edges: list[list[int]]) -> list[int]:
    """X) Topological Sort.

    not suitable for undirected

    1) DSU

    if a new edge is connecting to the root of one of the node,
    i.e. the two nodes of the new edge have the same roots,
    then there's a cycle

    time complexity: O(N), space complexity: O(N)
    * N is the number of connections, also nodes here
    """
    # prefer list over dict when 1-n is known to avoid collision
    # use +1 as index is from [1, n]
    parents = [0 for _ in range(len(edges) + 1)]

    def find(x):
        while parents[x]:
            x = parents[x]
        return x

    def union(x, y):
        root_x, root_y = find(x), find(y)

        if root_x == root_y:
            return False
        else:
            parents[root_x] = root_y
            return True

    for a, b in edges:
        if not union(a, b):
            return [a, b]
