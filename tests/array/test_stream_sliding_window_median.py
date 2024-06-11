from src.array.stream_sliding_window_median import slidingWindowMedian


def testSlidingWindowMedian():
    assert slidingWindowMedian([5, 4, 3, 2, 1, 2, 6, 7, 8], 5) == [
        3.0,
        2.0,
        2.0,
        2.0,
        6.0,
    ]
    assert slidingWindowMedian([1, 3, -1, -3, 5, 3, 6, 7], 3) == [
        1.0,
        -1.0,
        -1.0,
        3.0,
        5.0,
        6.0,
    ]
    assert slidingWindowMedian([1, 2, 3, 4, 2, 3, 1, 4, 2], 3) == [
        2.0,
        3.0,
        3.0,
        3.0,
        2.0,
        3.0,
        2.0,
    ]
