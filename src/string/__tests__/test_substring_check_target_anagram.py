from src.string.substring_check_target_anagram import check_inclusion


def testCheckInclusion():
    assert check_inclusion("ab", "eidbaooo") is True
    assert check_inclusion("ab", "eidboaoo") is False
    assert check_inclusion("abc", "cccccbabbbaaaa") is True
    assert check_inclusion("a", "ab") is True
