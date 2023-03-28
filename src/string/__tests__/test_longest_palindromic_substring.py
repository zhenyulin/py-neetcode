from src.string.longest_palindromic_substring import longestPalindrome


def testLongestPalindrom():
    assert longestPalindrome("babad") == "bab"
    assert longestPalindrome("adcba") == "a"
    assert longestPalindrome("cbbd") == "bb"
    assert longestPalindrome("aabbcc") == "aa"
