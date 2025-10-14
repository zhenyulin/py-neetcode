#
# 974. Subarray Sums Divisible by K
# https://leetcode.com/problems/subarray-sums-divisible-by-k/
#
from collections import defaultdict


def subarray_div_by_k(nums: list[int], k: int) -> int:
    """To count all subarray sum divisible by k.

    1) Hashmap Prefix Sum, {sum: count}1

    time complexity: O(N), space complexity: O(N)
    """
    res, acc = 0, 0
    counter: dict[int, int] = defaultdict(int)

    for n in [0, *nums]:
        acc = (acc + n) % k
        res += counter.get(acc, 0)
        counter[acc] += 1

    return res
