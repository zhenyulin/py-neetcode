#
# 1091. Shortest Path in Binary Matrix
# https://leetcode.com/problems/shortest-path-in-binary-matrix/
#
from collections import deque


def shortestPath(grid: list[list[int]]) -> int:
    """to find the length of shortest path from top left to bottom right

    there are various trajectories from each step, to count the smallest level

    X) DFS
    target trajectories are unknown

    1) BFS
    find out all cells that can possibly be visited by N steps
    then as soon as destination can be reached, return steps

    * this avoided going backwards

    time complexity: O(N^2), space complexity: O(N^2)
    """

    if (grid[0][0], grid[-1][-1]) != (0, 0):
        return -1

    N = len(grid)

    OFFSETS = [(i, j) for i in [-1, 0, 1] for j in [-1, 0, 1] if (i, j) != (0, 0)]

    queue, visited, length = deque([(0, 0)]), set((0, 0)), 1

    while queue:
        for _ in range(len(queue)):

            # { search from }
            x, y = queue.popleft()

            # { target condition }
            if (x, y) == (N - 1, N - 1):
                return length

            # { search options }
            for dx, dy in OFFSETS:
                nx, ny = x + dx, y + dy
                # { search conditions }
                if (
                    0 <= nx < N
                    and 0 <= ny < N
                    and (nx, ny) not in visited
                    and grid[nx][ny] == 0
                ):
                    queue.append((nx, ny))
                    visited.add((nx, ny))

        length += 1

    return -1
