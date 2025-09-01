#
# 1574. Shortest Subarray to be Removed to Make Array Sorted
# https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/
#


def find_shortest_subarray_to_remove(arr: list[int]) -> int:
    """1) Greedy Sliding Window.

    we can firstly find the 'a', 'b' for [:a+1] and [b:] to be sorted
    a+1 >= b would be impossible, as that would mean the whole array is sorted
    and for [a+1: b] we still need to remove part in [:a+1] and [b:] so that they can be connected
    """
    n = len(arr)

    a = 0
    while a + 1 < n and arr[a + 1] >= arr[a]:
        a += 1

    if a == n - 1:
        return 0

    b = n - 1
    while b > 0 and arr[b] >= arr[b - 1]:
        b -= 1

    res = min(n - 1 - a, b)

    i, j = 0, b

    while i <= a and j < n:
        if arr[i] <= arr[j]:
            res = min(res, j - 1 - i)
            i += 1
        else:
            j += 1

    return res
