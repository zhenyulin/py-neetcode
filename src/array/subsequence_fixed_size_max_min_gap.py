#
# Global Maximum
#
# Consider an array of distinct positive intergers where the elements are sorted
# in ascending order. We want to find all the subsequences of the array consisting
# of exactly m elements. And we want to find the globalMaximum with the following pseuocode:
#
# globalMaximum = 0
#
# for each subsequence s, consiting of m elements {
#   currentMin = inf
#
#   for each (x, y) pair of elements in subsequence s {
#       diff = abs(x-y)
#
#       currentMin = min(currentMin, diff)
#   }
#
#   globalMax = max(globalMax, currentMin)
# }
#
# For example, [2,3,5,9] and length m=3, result would be 3
#


def maxMinGap(nums: list[int], m: int) -> int:
    """
    Given the array is sorted, we can probably leveraging BS

    1) Binary Search + Greedy

    we list out the possible range[min, max] of gap in the nums
    and using binary search to check the max subsequence gap

    for checking wether a gap can be achieved for the given nums and m
    we use greedy iterating the nums and counting gap larger than the target

    since all gaps are being used and we move to check new gap sum as soon as
    it passes the target, so this would be the leanest subsequence

    time complexity: O(Log(X)*N), space complexity: O(1)
    * X = nums[-1] - nums[0]
    """

    def possible(gap: int) -> bool:
        last, i = nums[0], 1
        for _ in range(m - 1):
            while i < len(nums) and nums[i] - last < gap:
                i += 1
            if i == len(nums):
                return False
            last = nums[i]
        return True

    i, j = 0, nums[-1] - nums[0]

    # avoid stuck on possible(i)
    while i < j - 1:
        mid = (i + j) // 2

        if possible(mid):
            i = mid
        else:
            j = mid - 1

    return j if possible(j) else i
