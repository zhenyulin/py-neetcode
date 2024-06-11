#
# 1901. Find a Peak Element II
# https://leetcode.com/problems/find-a-peak-element-ii/
#


def findPeakGrid(grid: list[list[int]]) -> list[int]:
    """Related to 1D peak element search.

    there are local peaks in every row or column
    it is basically to find a 2D peak from those local peaks

    between column max [a, b] and nearest 2D peak <x, y>

        [a, b] ****** ****** (x, b) ******
        ****** ****** ****** ****** ******
        (a, y) ****** ****** <x, y> ******

    both [a, b] and <x, y> would be higher than (a, y)
    <x, y> is higher than (x, b), while (a, b) could be higher or lower
    there can only be a path if [a, b] is lower than (x, b)
        [a, b] -> (x, b) -> <x, y>
    e.g. we need to search on the side where condition is not met
    which is equivalent to binary search

    we start from column max instead of peak, then using binary search
    to narrow down our scope to find the column of 2D peak
    this way, we are only getting to larger values (climbing uphills)

    2D binary search can land us in column peak instead of max

    1) Binary Search x Greedy

    find the first column peak, and then check if it is 2D peak
    if not continue searching on the ascending side (where condition not met)

    time complexity: O(M*LogN), space complexity: O(1)

    """
    left, right = 0, len(grid[0]) - 1

    while left <= right:
        m = (left + right) // 2

        i_max = 0
        for i in range(len(grid)):
            if grid[i][m] > grid[i_max][m]:
                i_max = i

        left_condition = m == 0 or grid[i_max][m - 1] < grid[i_max][m]
        right_condition = m == len(grid[0]) - 1 or grid[i_max][m + 1] < grid[i_max][m]

        if left_condition and right_condition:
            return [i_max, m]
        elif right_condition:
            right = m
        else:
            left = m + 1

    return None
