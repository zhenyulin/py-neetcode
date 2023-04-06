from src.array_2d.search_length_shortest_path import shortestPath


def testShortestPath():
    assert (
        shortestPath(
            [
                [0, 1],
                [1, 0],
            ]
        )
        == 2
    )

    assert (
        shortestPath(
            [
                [0, 0, 0],
                [1, 1, 0],
                [1, 1, 0],
            ]
        )
        == 4
    )

    assert (
        shortestPath(
            [
                [1, 0, 0],
                [1, 1, 0],
                [1, 1, 0],
            ]
        )
        == -1
    )
