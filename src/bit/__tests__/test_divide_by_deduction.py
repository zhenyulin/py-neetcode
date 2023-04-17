from src.bit.divide_by_deduction import divide


def testDivide():
    assert divide(10, 3) == 3
    assert divide(7, -3) == -2
