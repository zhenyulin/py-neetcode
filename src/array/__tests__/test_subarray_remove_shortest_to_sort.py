from src.array.subarray_remove_shortest_to_sort import findShortestSubarrayToRemove


def testFindShortestSubarrayToRemove():
    assert findShortestSubarrayToRemove([1, 2, 3, 10, 4, 2, 3, 5]) == 3
    assert findShortestSubarrayToRemove([5, 4, 3, 2, 1]) == 4
    assert findShortestSubarrayToRemove([1, 2, 3]) == 0
