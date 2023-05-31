#
# Friend Circle Queries
# https://www.hackerrank.com/challenges/friend-circle-queries/problem
#
from collections import defaultdict


def largestGroup(queries: list[list[int]]) -> list[int]:
    """

    1) DSU(Disjoint Set Union | Root Union)

    we can use a graph to record the connections of nodes
    upon taking a new connection, we can update the graph, search its root
    and update the group size recorded as dict with group represented by root

    time complexity: O(C), space complexity: O(N)

    *C is the number of queries(connections), N is the number of nodes
    *M is the number of groups, can be considered as constant
    """

    res, anchors, sizes = [0], {}, defaultdict(lambda: 1)

    # nodes are only pointed to its root at connect time
    # so may be out-dated to only anchors not roots with later queries
    # that's why it is called disjoint set
    def root(x):
        while x in anchors:
            x = anchors[x]
        return x

    def root_union(x, y):
        root_x, root_y = root(x), root(y)
        if root_x != root_y:
            anchors[root_y] = root_x
            sizes[root_x] += sizes[root_y]

    for a, b in queries:
        root_union(a, b)
        res.append(max(res[-1], sizes[root(a)]))

    return res[1:]

    """

    2) Greedy:

    we can use sets to record individual groups
    add new nodes if found in existing group
    connect groups if one connection links two groups
    add new group if connected to no existing group

    time complexity: O(Q*M), space complexity: O(N)
    *Q is the number of queries, N is the number of nodes
    *M is the number of groups, can be considered as constant
    """

    # res, groups = [0], []

    # for a, b in queries:
    #     j, k = -1, -1

    #     for i, group in enumerate(groups):

    #         if j >= 0 and k >= 0:
    #             break
    #         elif j < 0 and a in group:
    #             group |= {a, b}
    #             j = i
    #         elif k < 0 and b in group:
    #             group |= {a, b}
    #             k = i

    #     if j < 0 and k < 0:
    #         groups.append({a, b})
    #         res.append(max(res[-1], 2))
    #     elif j >= 0 and k >= 0:
    #         groups[j] |= groups[k]
    #         # avoid the influence of index shift from pop
    #         res.append(max(res[-1], len(groups[j])))
    #         groups.pop(k)
    #     else:
    #         res.append(max(res[-1], len(groups[max(j, k)])))

    # return res[1:]
