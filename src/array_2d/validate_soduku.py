#
# 36. Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/
#
from collections import defaultdict


def isValidSudoku(board: list[list[str]]) -> bool:
    """0) Brutal Force:
    check each row, each column, each box separately
    time complexity: O(9*9*3), space complexity: O(9).

    1) Search with Memory:
    use a set to record each row, column and box iterating through the board

    time complexity: O(9*9), space complexity: O(9*9*3)
    """
    rows, cols, squares = defaultdict(set), defaultdict(set), defaultdict(set)

    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                continue
            if (
                board[i][j] in rows[i]
                or board[i][j] in cols[j]
                or board[i][j] in squares[(i // 3, j // 3)]
            ):
                return False

            rows[i].add(board[i][j])
            cols[j].add(board[i][j])
            squares[(i // 3, j // 3)].add(board[i][j])

    return True
