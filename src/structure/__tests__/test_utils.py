from src.structure.utils import binary_search_index


def testBinarySearchIndex():
    assert binary_search_index([], 1) == 0
    assert binary_search_index([0], 1) == 1
    assert binary_search_index([2], 1) == 0
    assert binary_search_index([1, 3], 0) == 0
    assert binary_search_index([1, 3], 2) == 1
    assert binary_search_index([1, 3], 4) == 2
    assert binary_search_index([1, 3, 5], 0) == 0
    assert binary_search_index([1, 3, 5], 1) == 1
    assert binary_search_index([1, 3, 5], 2) == 1
    assert binary_search_index([1, 3, 5], 3) == 2
    assert binary_search_index([1, 3, 5], 4) == 2
    assert binary_search_index([1, 3, 5], 5) == 3
    assert binary_search_index([1, 3, 5], 6) == 3
    assert binary_search_index([1, 3, 5, 7], 0) == 0
    assert binary_search_index([1, 3, 5, 7], 2) == 1
    assert binary_search_index([1, 3, 5, 7], 4) == 2
    assert binary_search_index([1, 3, 5, 7], 6) == 3
    assert binary_search_index([1, 3, 5, 7], 8) == 4


def testBinarySearchIndexDescending():
    reverse_binary_search_index = lambda *args, **kwargs: binary_search_index(
        *args, ascending=False, **kwargs
    )
    assert reverse_binary_search_index([], 1) == 0
    assert reverse_binary_search_index([0], 1) == 0
    assert reverse_binary_search_index([2], 1) == 1
    assert reverse_binary_search_index([3, 1], 0) == 2
    assert reverse_binary_search_index([3, 1], 2) == 1
    assert reverse_binary_search_index([3, 1], 4) == 0
    assert reverse_binary_search_index([5, 3, 1], 6) == 0
    assert reverse_binary_search_index([5, 3, 1], 5) == 0
    assert reverse_binary_search_index([5, 3, 1], 4) == 1
    assert reverse_binary_search_index([5, 3, 1], 3) == 1
    assert reverse_binary_search_index([5, 3, 1], 2) == 2
    assert reverse_binary_search_index([5, 3, 1], 1) == 2
    assert reverse_binary_search_index([5, 3, 1], 0) == 3
