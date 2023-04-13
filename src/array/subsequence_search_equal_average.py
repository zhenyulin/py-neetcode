#
# 805. Split Array With Same Average
# https://leetcode.com/problems/split-array-with-same-average/
#


def subsequenceEqualAverage(arr: list[int]) -> bool:
    """
    subsequence search with condition

    1) Dynamic Programming

    we can record all possible sums of subsequence size between (0, N//2)
    then check if any sum matches 'sum * len(A) == total * size'
    equivalent to 'sum/size == total/len(A)' but without floating point

    time complexity: O(N^N), space complexity: O(N^N) ~ C(N, N//2) ~ N^(N//2)
    """

    # arr.sort(reverse=True)

    # TOTAL, N = sum(arr), len(arr)
    # HALF = TOTAL / 2

    # # dp[i] denotes possible sum at size N//2-i between (N//2, 0)
    # dp = [set() for _ in range(N // 2)] + [{0}]

    # for a in arr:

    #     for i in range(len(dp) - 1):
    #         # from smaller size
    #         for s in dp[i + 1]:
    #             if s + a <= HALF:
    #                 dp[i].add(s + a)

    # for i in range(len(dp) - 1):
    #     if TOTAL * (N // 2 - i) in [s * N for s in dp[i]]:
    #         return True

    # return False

    """
    2) Math

    each 'n' in arr can be updated to its deviation from the average
    'n - total/len(arr)', which can be reformed to int 'n * len(arr) - total'
    then we just need to find the subsequence with a zero sum of deviations
    """

    total, N = sum(arr), len(arr)

    arr, sums = [a * N - total for a in sorted(arr)], set()

    for a in arr[:-1]:
        # for sorted arr, a is increasing, therefore only check s + a <= 0
        sums |= {a} | {a + s for s in sums if s + a <= 0}
        if 0 in sums:
            return True

    return False
