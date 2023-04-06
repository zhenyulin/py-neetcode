from src.string.two_strings_subsequence_longest_common import longestCommonSubsequence


def testLongestCommonSubsequence():
    assert longestCommonSubsequence("abcde", "ace") == 3
    assert longestCommonSubsequence("abc", "abc") == 3
    assert longestCommonSubsequence("abc", "def") == 0
