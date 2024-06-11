#
# 695. Max Area of Island
# https://leetcode.com/problems/max-area-of-island/
#


def longestPath(grid: list[list[int]]) -> int:
    """For longest path.

    1) DFS

    time complexity: O(M*N), space complexity: O(1)
    """
    res, M, N = 0, len(grid), len(grid[0])

    def dfs(i, j):
        if grid[i][j] == 0:
            return 0

        grid[i][j] = 0  # mark visited in place

        area = 1
        area += dfs(i - 1, j) if 0 <= i - 1 else 0
        area += dfs(i + 1, j) if i + 1 < M else 0
        area += dfs(i, j - 1) if 0 <= j - 1 else 0
        area += dfs(i, j + 1) if j + 1 < N else 0

        return area

    for i in range(M):
        for j in range(N):
            res = max(res, dfs(i, j))

    return res
