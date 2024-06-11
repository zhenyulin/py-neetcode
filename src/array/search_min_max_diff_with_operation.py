#
# 910. Smallest Range II
# https://leetcode.com/problems/smallest-range-ii/
#


def smallestRange(nums: list[int], k: int) -> int:
    """We need to find the possible cloest new min and new max to reduce the gap.

    for any pair (a, b) with a <= b in the list,
    only (a+k, b-k) can possibly reduce the gap to |b-a-2k|

        1) (b-a-2k) when n'<=a'<=b'<=m', b-a >= 2k, new gap -> [0,inf]
        2) -(b-a-2k) when b'<=a', b-a <= 2k, new gap -> [0, 2K]

    *n'=n+k, a'=a+k, b'=b-k, m'=m-k
    *n'<=a', b'<=m'

    for 1) the new min, max for the nums would be n', m'

    for 2) there are 5 further cases:
        a) b', m', n', a'
        b) b', n', m', a'
        c) b', n', a', m'
        d) n', b', m', a'
        e) n', b', a', m'

    the possible new min is within (b', n'), possible new max within (a', m')

    combine the two situations, we can examine max(a', m') - min(b', n') at each (a, b)

    to ensure iterating through nums as pair, each n is examined twice as a and b
    we need to sort the list to ensure a <= b

    1) Greedy

    we can init with res as 'm - n' with non-update operations
    find the possible candidates, rolling update res

    time complexity: O(N), space complexity: O(1)
    """
    nums.sort()

    n, m = nums[0], nums[-1]
    res = m - n

    for a, b in zip(nums[:-1], nums[1:]):

        res = min(res, max(m - k, a + k) - min(n + k, b - k))

    return res
