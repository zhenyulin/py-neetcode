#
# 560. Subarray Sum Equals K
# https://leetcode.com/problems/subarray-sum-equals-k/
#

from collections import defaultdict


def subarray_sum(nums: list[int], k: int) -> int:
    """To count all subarray sum up to k.

    1) Hashmap Prefix Sum, {sum: count}

        sum[i:j] = sum[:j] - sum[:i]

    once we use prefix sum, it is very similar to 1. Two Sum
    instead of finding indexes, we are counting all combos

    time complexity: O(N), space complexity: O(N)
    """
    res, acc = 0, 0
    counter: dict[int, int] = defaultdict(int)

    # to have counter[0], i.e. sum[:0], as 0
    for n in [0, *nums]:
        acc += n
        # current - target == k
        res += counter.get(acc - k, 0)
        counter[acc] += 1

    return res
