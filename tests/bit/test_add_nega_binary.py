from src.bit.add_nega_binary import addNegaBinary


def testAddNegaBinary():
    assert addNegaBinary([1, 1, 1, 1, 1], [1, 0, 1]) == [1, 0, 0, 0, 0]
    assert addNegaBinary([1], [1]) == [1, 1, 0]
    assert addNegaBinary([1], [1, 1]) == [0]
