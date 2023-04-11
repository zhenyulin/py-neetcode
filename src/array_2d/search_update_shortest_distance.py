#
# 286. Walls and Gates
# https://tenderleo.gitbooks.io/leetcode-solutions-/content/GoogleMedium/286.html
#
from collections import deque


def updateEmptyRooms(grid: list[list[int]]) -> list[list[int]]:
    """to find the shortest path of empty rooms to gates

    1) BFS
    classic for shortest path, and 'visited' isn't needed with in-place updates

    time complexity: O(M*N), space complexity: O(1)
    """

    M, N, OFFSETS = len(grid), len(grid[0]), [(-1, 0), (1, 0), (0, -1), (0, 1)]
    gates = [(i, j) for i in range(M) for j in range(N) if grid[i][j] == 0]
    queue, distance = deque(gates), 1

    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()

            for dx, dy in OFFSETS:
                nx, ny = x + dx, y + dy

                if 0 <= nx < M and 0 <= ny < N and grid[nx][ny] == 2147483647:
                    grid[nx][ny] = distance
                    queue.append((nx, ny))

        distance += 1

    return grid
