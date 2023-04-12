from src.string.subsequence_count_match_target import numMatchSubsequences


def testNumMatchSubsequences():
    assert numMatchSubsequences("rabbbit", "rabbit") == 3
    assert numMatchSubsequences("babgbag", "bag") == 5
