#
# 15. 3Sum
# https://leetcode.com/problems/3sum/
#

from itertools import combinations


def threeSum(nums: list[int]) -> list[list[int]]:
    """0) Iteraive Greedy (Two Sum).

    time complexity: O(N^2), space complexity: O(N)
    """
    # res = set()

    # for i, n in enumerate(nums[:-2]):
    #     indexes = {}
    #     for j in range(i + 1, len(nums)):
    #         if -n - nums[j] in indexes:
    #             res.add(tuple(sorted([n, -n - nums[j], nums[j]])))
    #         indexes[nums[j]] = j

    # return [list(x) for x in res]

    """
    1) Greedy, Negative Positive Search

    shift the number by target k, make negative, positive list, set

    time complexity: O((N^2)/2), space complexity: O(N)
    """

    negatives, positives, zeros = [], [], 0

    for n in nums:
        if n < 0:
            negatives.append(n)
        elif n > 0:
            positives.append(n)
        else:
            zeros += 1

    res, N, P = set(), set(negatives), set(positives)

    if zeros:
        for n in N:
            if -n in P:
                res.add((n, 0, -n))

        if zeros > 2:
            res.add((0, 0, 0))

    for options, other in [negatives, P], [positives, N]:
        for x, y in combinations(options, 2):
            if -(x + y) in other:
                res.add(tuple(sorted([x, y, -(x + y)])))

    return [list(x) for x in res]
