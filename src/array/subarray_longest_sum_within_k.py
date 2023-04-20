# Input : arr[] = [1, 2, 1, 0, 1, 1, 0], k = 4
# Output : 5
# Explanation:
#  {1, 2, 1} => sum = 4, length = 3
#  {1, 2, 1, 0}, {2, 1, 0, 1} => sum = 4, length = 4
#  {1, 0, 1, 1, 0} =>5 sum = 3, length = 5


def longestSumWithinK(arr: list[int], k: int) -> int:
    """
    longest subarray on condition

    1) Sliding Window

    using sum condition, i <= j is always true
    to avoid j going out of bound, j < len(arr) - 1

    time complexity: O(N), space complexity: O(1)
    """

    res, i, j, current = 0, 0, 0, arr[0]

    while i < len(arr) and j < len(arr) - 1:

        # { expand right condition }
        if current <= k:
            j += 1
            current += arr[j]

        # { try expand left, in case arr[j] < 0 }
        while current <= k and i > 0:
            i -= 1
            current += arr[i]

        # { contract left condition }
        if current > k:
            current -= arr[i]
            i += 1

        res = max(res, j - i + 1)

    return res
