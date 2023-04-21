from src.array.subsequence_fixed_size_max_min_gap import maxMinGap


def testMaxMinGap():
    assert maxMinGap([2, 3, 5, 9], 3) == 3
    assert maxMinGap([2, 3, 8, 12, 13], 3) == 5
