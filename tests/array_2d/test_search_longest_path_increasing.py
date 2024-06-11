from src.array_2d.search_longest_path_increasing import longestIncreasingPath


def TestLongestIncreasingPath():
    grid = [
        [9, 9, 4],
        [6, 6, 8],
        [2, 1, 1],
    ]
    assert longestIncreasingPath(grid) == 4

    grid = [
        [3, 4, 5],
        [3, 2, 6],
        [2, 2, 1],
    ]
    assert longestIncreasingPath(grid) == 4

    assert longestIncreasingPath([[1]]) == 1
