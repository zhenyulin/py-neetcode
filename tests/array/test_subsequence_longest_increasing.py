from src.array.subsequence_longest_increasing import longestIncreasingSubsequence


def testLongestIncreasingSubsequence():

    assert longestIncreasingSubsequence([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert longestIncreasingSubsequence([0, 1, 0, 3, 2, 3]) == 4
    assert longestIncreasingSubsequence([7, 7, 7, 7, 7, 7, 7]) == 1
