#
# Triplets
#  Given an array of 'n' distinct intergers and an integer threshold 't'
# How many (a, b, c) index triplets satisfying the following conditions:
# - d[a] < d[b] < d[c]
# - d[a] + d[b] + d[c] <= k
#


def countTriplets(arr: list[int], t: int) -> int:
    """
    1) Iteration + Sliding Window

    time complexity: O(N^2), space complexity: O(1)
    """

    arr.sort()

    res = 0

    for a in range(len(arr) - 2):
        b, c = a + 1, len(arr) - 1

        while b < c:
            if arr[a] + arr[b] + arr[c] <= t:
                # (b+1, c) can all be eligible for c
                res += c - b
                b += 1
            else:
                c -= 1

    return res
