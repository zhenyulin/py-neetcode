#
# Friend Circle Queries
# https://www.hackerrank.com/challenges/friend-circle-queries/problem
#


def largestGroup(queries: list[list[int]]) -> list[int]:
    """
    we can use sets to record individual groups

    1) Greedy:

    time complexity: O(N*M), space complexity: O(N)

    *M is the number of groups, can be considered as constant
    """

    res, groups = [0], []

    for a, b in queries:
        j, k = -1, -1

        for i, group in enumerate(groups):

            if j >= 0 and k >= 0:
                break
            elif j < 0 and a in group:
                group |= {a, b}
                j = i
            elif k < 0 and b in group:
                group |= {a, b}
                k = i

        if j < 0 and k < 0:
            groups.append({a, b})
            res.append(max(res[-1], 2))
        elif j >= 0 and k >= 0:
            groups[j] |= groups[k]
            # avoid the influence of index shift from pop
            res.append(max(res[-1], len(groups[j])))
            groups.pop(k)
        else:
            res.append(max(res[-1], len(groups[max(j, k)])))

    return res[1:]
