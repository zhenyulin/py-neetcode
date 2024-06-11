#
# 79. Word Search
# https://leetcode.com/problems/word-search/
#
# from collections import defaultdict, Counter


def exist(board: list[list[str]], word: str) -> bool:
    """2D search, we can use.

    1) DFS
    use a 'used' set to record the cells used

    time complexity: O(M*N*4^W), space complexity: O(1)
    """
    M, N, path = len(board), len(board[0]), set()

    def dfs(i, j, w):
        # { the target condition }
        if w == len(word):
            return True

        # { the search condition }
        if 0 <= i < M and 0 <= j < N and board[i][j] == word[w] and (i, j) not in path:
            path.add((i, j))

            # { the search directions }
            # the conditional return using for-loop implementation
            for ni, nj in (i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1):
                if dfs(ni, nj, w + 1):
                    return True

            # the or statements implementation, remember to return res
            # res = (
            #     dfs(i + 1, j, w + 1)
            #     or dfs(i - 1, j, w + 1)
            #     or dfs(i, j - 1, w + 1)
            #     or dfs(i, j + 1, w + 1)
            # )

            path.remove((i, j))

            # return res

    # optional: reverse the word if frequency of the first letter is more than the last letter's
    # count = defaultdict(int, sum(map(Counter, board), Counter()))
    # if count[word[0]] > count[word[-1]]:
    #     word = word[::-1]

    for i in range(M):
        for j in range(N):
            # { return if found }
            if dfs(i, j, 0):
                return True

    return False
