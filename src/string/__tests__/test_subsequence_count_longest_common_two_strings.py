from src.string.subsequence_count_longest_common_two_strings import (
    longestCommonSubsequence,
)


def testLongestCommonSubsequence():
    assert longestCommonSubsequence("abcde", "ace") == 3
    assert longestCommonSubsequence("abc", "abc") == 3
    assert longestCommonSubsequence("abc", "def") == 0
