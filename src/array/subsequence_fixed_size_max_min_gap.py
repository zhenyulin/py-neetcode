#
# 1552. Magnetic Force Between Two Balls
# https://leetcode.com/problems/magnetic-force-between-two-balls/description/
#


def max_min_gap(nums: list[int], m: int) -> int:
    """Given the array is sorted, we can probably leveraging BS.

    1) Binary Search + Greedy

    we list out the possible range[min, max] of gap in the nums
    and using binary search to check the max subsequence gap

    # for checking whether a gap can be achieved for the given nums and m
    we use greedy iterating the nums and counting gap larger than the target

    since all gaps are being used and we move to check new gap sum as soon as
    it passes the target, so this would be the leanest subsequence

    time complexity: O(Log(X)*N), space complexity: O(1)
    * X = nums[-1] - nums[0]
    """

    def possible(gap: int) -> bool:
        last, count = nums[0], m - 1
        for n in nums[1:]:
            if n - last >= gap:
                last = n
                count -= 1
                if count == 0:
                    return True
        return False

    nums.sort()
    l, r = 0, nums[-1] - nums[0]

    while l <= r:
        mid = (l + r) // 2

        if possible(mid):
            l = mid + 1  # avoid stuck on l when r == l + 1
        else:
            r = mid - 1

    return l - 1
