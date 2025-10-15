#
# 84. Largest Rectangle in Histogram
# https://leetcode.com/problems/largest-rectangle-in-histogram/
#


def largest_area_rectangle(heights: list[int]) -> int:
    """Largest area rectangle.

    To get the max rectangle area, we need an effective data structure
    to record all viable previous heights to heights[i] to form a larger rectangle.

    1) Sliding Window & Stack

    when iterate through heights, we can use a stack to record and accumulate
    (i, h), where i is the start index where heights[i:j] > heights[j]
    at each step we will unload all previous records that can form rectangle with height[j]
    and calculate the area by (j-1-i+1)*height[i]
    and then update the record with earliest index for height[j]

    time complexity: O(N), space complexity: O(N)
    """
    res = 0
    stack: list[tuple[int, int]] = []

    # append a 0 height to unload remaining stack in the end
    for i, h in enumerate([*heights, 0]):
        left = i
        # keep the stack[0][1] height <= h, and unload when shorter h found
        while stack and stack[-1][1] > h:
            left, height = stack.pop()
            res = max(res, (i - left) * height)
        stack.append((left, h))

    return res
