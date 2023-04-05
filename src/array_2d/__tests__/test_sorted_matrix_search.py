from src.array_2d.sorted_matrix_search import search


def testSearch():
    assert (
        search(
            [
                [1, 3, 5, 7],
                [10, 11, 16, 20],
                [23, 30, 34, 60],
            ],
            3,
        )
        == True
    )
    assert (
        search(
            [
                [1, 3, 5, 7],
                [10, 11, 16, 20],
                [23, 30, 34, 60],
            ],
            13,
        )
        == False
    )
