from src.string.substring_count_equal_unique_chars_split import numSplit


def testNumSplit():
    assert numSplit("aacaba") == 2
    assert numSplit("abcd") == 1
