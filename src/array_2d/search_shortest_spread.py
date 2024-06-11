#
# 994. Rotting Oranges
# https://leetcode.com/problems/rotting-oranges/
#
from collections import deque


def shortestSpread(grid: list[list[int]]) -> int:
    """Shortest ~ BFS.

    1) BFS

    time complexity: O(M*N), space complexity: O(K)
    """
    M, N = len(grid), len(grid[0])
    turn, target, queue = 0, 0, deque()

    for i in range(M):
        for j in range(N):
            if grid[i][j] == 2:
                queue.append((i, j))
            elif grid[i][j] == 1:
                target += 1

    while target and queue:
        for _ in range(len(queue)):
            i, j = queue.popleft()

            for ni, nj in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= ni < M and 0 <= nj < N and grid[ni][nj] == 1:
                    grid[ni][nj] = 2
                    queue.append((ni, nj))
                    target -= 1

        turn += 1

    return -1 if target else turn
