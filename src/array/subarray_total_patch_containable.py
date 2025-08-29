#
# 42. Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/
#


def total_patch(heights: list[int]) -> int:
    """This can be related to 11. Container With Most Water (subarray max area containable).

    1) Greedy, Sliding Window
    we moving two pointers from both ends, check the height against its bounded bar
    at each index, and fill the value according to its bounded bar (containable)

    we want to make sure that we wouldn't be in the situation that the opposite bounded
    bar should be applied, so we are only going to update the bounded bar
    when its value is smaller than the other side

              |
        | |   |
        | | | |
        n,i,j,m

    at each (i, j), we can fill the smaller value with the last updated bar
    e.g. we will be filling j with (n-j) for the above, as n < m,
    n would be last updated bar

    time complexity: O(N), space complexity: O(1)
    """
    i, j = 0, len(heights) - 1
    fill, left_bar, right_bar = 0, 0, 0

    while i < j:
        if heights[i] > heights[j]:
            # update the bounded bar when its value is smaller
            # so that we are sure the bounded bar is shorter than the opposite
            right_bar = max(right_bar, heights[j])
            fill += right_bar - heights[j]
            j -= 1
        else:
            left_bar = max(left_bar, heights[i])
            fill += left_bar - heights[i]
            i += 1

    return fill
