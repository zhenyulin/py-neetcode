from src.array_2d.search_element_peak import findPeakGrid


def testFindPeakGrid():
    grid = [
        [1, 4],
        [3, 2],
    ]
    assert findPeakGrid(grid) in [[1, 0], [0, 1]]

    grid = [
        [10, 20, 15],
        [21, 30, 14],
        [7, 16, 32],
    ]
    assert findPeakGrid(grid) == [1, 1]

    grid = [
        [10, 20, 15, 10, 7, 4, 1],
        [40, 30, 14, 11, 8, 5, 2],
        [7, 16, 13, 12, 9, 6, 3],
    ]
    assert findPeakGrid(grid) == [1, 0]

    grid = [
        [10, 20, 15, 10, 7, 4, 1],
        [8, 21, 22, 11, 8, 5, 2],
        [7, 16, 23, 12, 9, 6, 3],
        [6, 30, 24, 11, 8, 5, 2],
    ]
    assert findPeakGrid(grid) == [3, 1]
