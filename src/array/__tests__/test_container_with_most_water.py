from src.array.container_with_most_water import maxArea


def testMaxArea():
    assert maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert maxArea([6, 11, 10, 1, 2, 3, 5, 4, 11, 7, 6]) == 77
