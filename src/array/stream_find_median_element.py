#
# 295. Find Median from Data Stream
# https://leetcode.com/problems/find-median-from-data-stream/
#


from heapq import heappop, heappush


class MedianFinder:
    """to find median element from a data stream

    1) Min Max Heaps
    keep the length difference of min, max heaps to be less than 1

    time complexity: O(1), space complexity: O(N)
    """

    def __init__(self):
        self.left = []  # max heap, descending
        self.right = []  # min heap, ascending

    def addNum(self, num: int) -> None:
        # prefer using the min heap so that less negative sign is needed
        # replace the smallest on the right, and move it to the left
        heappush(self.right, num)
        heappush(self.left, -heappop(self.right))

        # left heap is growing but not right, make len(left) <= len(right)
        if len(self.left) > len(self.right):
            heappush(self.right, -heappop(self.left))

    def findMedian(self) -> float:
        return (
            (self.right[0] - self.left[0]) / 2
            if len(self.left) == len(self.right)
            else self.right[0]
        )
