from src.array.subarray_addition_multiple import rangeAddition


def testRangeAddition():
    assert rangeAddition(5, [[1, 3, 2], [2, 4, 3], [0, 2, -2]]) == [-2, 0, 3, 5, 3]
