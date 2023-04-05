from src.array.subarray_min_size_sum import minSubArrayLen


def testMinSubArrayLen():
    assert minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2
    assert minSubArrayLen(4, [1, 4, 4]) == 1
    assert minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0
