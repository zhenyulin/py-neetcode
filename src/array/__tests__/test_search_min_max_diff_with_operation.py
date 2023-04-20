from src.array.search_min_diff_after_operations import smallestRange


def testSmallestRange():
    assert smallestRange([1], 0) == 0
    assert smallestRange([0, 10], 2) == 6
    assert smallestRange([1, 3, 6], 3) == 3
    assert smallestRange([2, 7, 2], 1) == 3
    assert smallestRange([3, 1, 10], 4) == 2
