from src.string.substring_longest_palindromic import longestPalindrome


def testLongestPalindrom():
    assert longestPalindrome("babad") == "bab"
    assert longestPalindrome("adcba") == "a"
    assert longestPalindrome("cbbd") == "bb"
    assert longestPalindrome("aabbcc") == "aa"
