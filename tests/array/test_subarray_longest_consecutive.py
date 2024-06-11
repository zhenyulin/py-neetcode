from src.array.subarray_longest_consecutive import longestConsecutiveSequence


def testLongestConsecutiveSequence():
    assert longestConsecutiveSequence([100, 4, 200, 1, 3, 2]) == 4
    assert longestConsecutiveSequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
