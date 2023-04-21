from src.array.two_arrays_min_path_cost import minCost


def testMinCost():
    assert minCost([2, 3, 4], [3, 1, 1], 2) == [0, 2, 5, 6]
