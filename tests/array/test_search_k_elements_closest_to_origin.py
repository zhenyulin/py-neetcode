from src.array.search_k_elements_closest_to_origin import kClosest


def testKClosest():
    assert kClosest([[1, 3], [-2, 2]], 1) == [[-2, 2]]
    assert kClosest([[3, 3], [5, -1], [-2, 4]], 2) == [[3, 3], [-2, 4]]
