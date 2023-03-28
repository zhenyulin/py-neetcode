from src.string.longest_substring_without_repeating_characters import (
    lengthOfLongestSubstring,
)


def testLengthOfLongestSubstring():
    assert lengthOfLongestSubstring("abcabcbb") == 3
    assert lengthOfLongestSubstring("pwwkew") == 3
    assert lengthOfLongestSubstring("bbbbb") == 1
    assert lengthOfLongestSubstring("") == 0
