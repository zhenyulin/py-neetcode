#
# 1574. Shortest Subarray to be Removed to Make Array Sorted
# https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/
#


def findShortestSubarrayToRemove(arr: list[int]) -> int:
    """1) Greedy Sliding Window:

    we can firstly find the 'a', 'b' for [:a+1] and [b:] to be sorted
    if there's something to be removed, then a < b
    then find the smallest window '[i, j]'' covering '[a+1:b-1]' so that arr[i] <= arr[j]
    """
    N = len(arr)

    a = 0
    while a + 1 < N and arr[a + 1] >= arr[a]:
        a += 1

    if a == N - 1:
        return 0

    b = N - 1
    while b > 0 and arr[b] >= arr[b - 1]:
        b -= 1

    res = min(N - 1 - a, b)

    i, j = 0, b

    while i <= a and j < N:
        if arr[i] <= arr[j]:
            res = min(res, j - 1 - i)
            i += 1
        else:
            j += 1

    return res
