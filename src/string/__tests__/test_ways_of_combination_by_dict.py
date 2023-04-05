from src.string.ways_of_combination_by_dict import waysOfDecoding


def testWaysOfDecoding():
    assert waysOfDecoding("12") == 2
    assert waysOfDecoding("226") == 3
    assert waysOfDecoding("06") == 0
