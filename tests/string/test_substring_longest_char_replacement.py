from src.string.substring_longest_char_replacement import charReplacement


def testCharReplacement():
    assert charReplacement("ABAB", 2) == 4
    assert charReplacement("AABABBA", 1) == 4
