from src.string.combination_dictionary_search_match_sum import isSolvable


def testIsSolvable():
    assert isSolvable(["SEND", "MORE"], "MONEY") == True
    assert isSolvable(["SIX", "SEVEN", "SEVEN"], "TWENTY") == True
    assert isSolvable(["LEET", "CODE"], "POINT") == False
