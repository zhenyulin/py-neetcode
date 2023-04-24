from src.graph.stream_largest_group import largestGroup


def testLargestGroup():
    assert largestGroup(
        [
            [1, 2],
            [3, 4],
            [2, 3],
        ]
    ) == [2, 2, 4]

    assert largestGroup(
        [
            [1000000000, 23],
            [11, 3778],
            [7, 47],
            [11, 1000000000],
        ]
    ) == [2, 2, 2, 4]

    assert largestGroup(
        [
            [1, 2],
            [3, 4],
            [1, 3],
            [5, 7],
            [5, 6],
            [7, 4],
        ]
    ) == [2, 2, 4, 4, 4, 7]

    assert largestGroup(
        [
            [1, 2],
            [3, 4],
            [1, 3],
            [7, 5],
            [6, 5],
            [7, 4],
        ]
    ) == [2, 2, 4, 4, 4, 7]
