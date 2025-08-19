#
# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/
#


def max_area(height: list[int]) -> int:
    """Find the max area that can be held by two heights from the input.

    0) Brutal Force:
    at each possible 'width', we want to use the possible max 'bar' (min height)
    and compare and update the 'res' with the 'area'

    1) Greedy & Two Pointers (Two Way Iteration):

    we can start from max 'width' where there's only one possible option of heights
    as the 'width' shrinks, the only way to find a bigger area is to find a larger 'bar'

    when shrinking the width, the only way to potentially find a bigger 'bar'
    is to move the smaller 'height' in the 'bar' (it may get smaller)

    * moving the other way, 'bar' won't get bigger
    * the only possible situation to produce a larger area when shrinking width is
    that for [l, l', r', r] that min(l', r') > min(l, r), and
    1) one of l', r' will firstly be reached by simply moving l or r
    2) in cases of (l, r'), or (l', r), r' > l or l' > r, so it would converge to (l', r')
    the possibility wouldn't be missed using this method


    time complexity: O(N), space complexity: O(1)
    """
    l, r, bar, res = 0, len(height) - 1, 0, 0

    while l < r:
        bar = min(height[l], height[r])
        res = max(res, bar * (r - l))

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return res
