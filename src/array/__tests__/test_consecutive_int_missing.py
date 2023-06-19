from src.array.consecutive_int_missing import missingNumber


def testMissingNumber():
    assert missingNumber([3, 0, 1]) == 2
    assert missingNumber([0, 1]) == 2
    assert missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
