from src.tree.invert import invert


def testInvert():
    assert invert([4, 2, 7, 1, 3, 6, None]) == [4, 7, 2, None, 6, 3, 1]
    assert invert([2, 1, 3]) == [2, 3, 1]
    assert invert([]) == []
