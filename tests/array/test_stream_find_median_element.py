from src.array.stream_find_median_element import MedianFinder


def testMedianFinder():
    stream = MedianFinder()
    stream.addNum(1)
    stream.addNum(2)
    assert stream.findMedian() == 1.5
    stream.addNum(3)
    assert stream.findMedian() == 2
