from src.array.subarray_max_area_rectangle import largestAreaRectangle


def testLargestAreaRectangle():
    assert largestAreaRectangle([2, 1, 5, 6, 2, 3]) == 10
    assert largestAreaRectangle([2, 4]) == 4
