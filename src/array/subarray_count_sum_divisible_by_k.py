#
# 974. Subarray Sums Divisible by K
# https://leetcode.com/problems/subarray-sums-divisible-by-k/
#
from collections import defaultdict


def subarrayDivByK(nums: list[int], k: int) -> int:
    """To count all subarrays sum divisible by k.

    1) Hashmap Prefix Sum, {sum: count}

    time complexity: O(N), space complexity: O(N)
    """
    res, current, counter = 0, 0, defaultdict(int)

    for n in [0] + nums:

        current = (current + n) % k
        res += counter.get(current, 0)
        counter[current] += 1

    return res
