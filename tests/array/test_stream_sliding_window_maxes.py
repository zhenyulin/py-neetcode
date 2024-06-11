from src.array.stream_sliding_window_maxes import windowMaxes


def testWindowMaxes():
    assert windowMaxes([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert windowMaxes([1], 1) == [1]
