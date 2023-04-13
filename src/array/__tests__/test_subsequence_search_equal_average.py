from src.array.subsequence_search_equal_average import subsequenceEqualAverage


def testSubsequenceEqualAverage():
    assert subsequenceEqualAverage([1, 2, 3, 4, 5, 6, 7, 8]) is True
    assert subsequenceEqualAverage([3, 1]) is False
    assert subsequenceEqualAverage([3, 1, 2]) is True
