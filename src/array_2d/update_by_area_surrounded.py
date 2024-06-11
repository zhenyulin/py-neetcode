#
# 130. Surrounded Regions
# https://leetcode.com/problems/surrounded-regions/
#
from collections import deque


def update(board: list[list[str]]) -> list[list[str]]:
    """Area surrounded, so only areas from the edges would be unsurrounded.

    1) DFS

    time complexity: O(M*N), space complexity: O(M+N)
    """
    # M, N = len(board), len(board[0])

    # def dfs(i, j):
    #     if 0 <= i < M and 0 <= j < N and board[i][j] == "O":
    #         board[i][j] = "E"
    #         dfs(i + 1, j)
    #         dfs(i - 1, j)
    #         dfs(i, j + 1)
    #         dfs(i, j - 1)

    # # escape from the edges
    # for i, j in [
    #     *[(i, j) for i in [0, M - 1] for j in range(N)],
    #     *[(i, j) for j in [0, N - 1] for i in range(M)],
    # ]:
    #     dfs(i, j)

    # # update
    # for i in range(1, M - 1):
    #     for j in range(1, N - 1):
    #         if board[i][j] == "O":
    #             board[i][j] = "X"

    # # recover escaped
    # for i in range(M):
    #     for j in range(N):
    #         if board[i][j] == "E":
    #             board[i][j] = "O"

    # return board

    """

    2) BFS
    from the edges

    time complexity: O(M*N), space_complexity: O(M+N)
    """
    M, N = len(board), len(board[0])

    edge_areas = [
        *[(i, j) for i in [0, M - 1] for j in range(N) if board[i][j] == "O"],
        *[(i, j) for j in [0, N - 1] for i in range(M) if board[i][j] == "O"],
    ]

    searches = deque(edge_areas)

    while searches:
        for _ in range(len(searches)):
            i, j = searches.popleft()
            for ni, nj in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 < ni < M - 1 and 0 < nj < N - 1 and board[ni][nj] == "O":
                    board[ni][nj] = "E"
                    searches.append((ni, nj))

    # update
    for i in range(1, M - 1):
        for j in range(1, N - 1):
            if board[i][j] == "O":
                board[i][j] = "X"

    # recover escaped
    for i in range(M):
        for j in range(N):
            if board[i][j] == "E":
                board[i][j] = "O"

    return board
