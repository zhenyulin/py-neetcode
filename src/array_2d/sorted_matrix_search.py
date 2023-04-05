#
# 74. Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix/
#


def search(matrix: list[list[int]], target: int) -> bool:
    """
    since the matrix is sorted, we can

    1) Binary Search
    binary search to find the row covering target
    and then binary search the target at the row

    time complexity: O(Log(M*N)), space complexity: O(1)
    """

    ROWS, COLS = len(matrix), len(matrix[0])

    top, bot = 0, ROWS - 1
    while top <= bot:
        row = (top + bot) // 2
        if target > matrix[row][-1]:
            top = row + 1
        elif target < matrix[row][0]:
            bot = row - 1
        else:
            break

    if top > bot:
        return False

    l, r = 0, COLS - 1
    while l <= r:
        m = (l + r) // 2
        if target > matrix[row][m]:
            l = m + 1
        elif target < matrix[row][m]:
            r = m - 1
        else:
            return True

    return False
