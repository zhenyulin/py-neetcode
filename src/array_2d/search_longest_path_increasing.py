#
# 329. Longest Increasing Path in a Matrix
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
#
from functools import cache


def longestIncreasingPath(matrix: list[list[int]]) -> int:
    """to find longest path increasing

    1) cached DFS

    increasing condition means we don't need to record path

    time complexity: O(M*N), space complexity: O(M*N)

    2) 2D Dynamic Programming
    """

    M, N = len(matrix), len(matrix[0])

    @cache
    def dfs(i, j):
        # { the target or step value }
        return 1 + max(
            dfs(ni, nj)
            # { search condition }
            if 0 <= ni < M and 0 <= nj < N and matrix[ni][nj] > matrix[i][j] else 0
            # { search options }
            for ni, nj in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]
        )

    return max(dfs(i, j) for i in range(M) for j in range(N))
