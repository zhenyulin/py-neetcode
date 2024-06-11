from src.bit.add_by_bit import add


def testAdd():
    assert add(1, 2) == 3
    assert add(2, 3) == 5
    assert add(-3, 2) == -1
    assert add(-2, 3) == 1
