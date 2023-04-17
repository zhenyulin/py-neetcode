from src.string.splits_count_equal_unique_chars import numSplit


def testNumSplit():
    assert numSplit("aacaba") == 2
    assert numSplit("abcd") == 1
