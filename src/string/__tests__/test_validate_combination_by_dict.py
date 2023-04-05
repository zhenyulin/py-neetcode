from src.string.validate_combination_by_dict import wordBreak


def testWordBreak():
    assert wordBreak("leetcode", ["leet", "code"]) == True
    assert wordBreak("applepenapple", ["apple", "pen"]) == True
    assert wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False
    assert wordBreak("etle", ["leet"]) == False
