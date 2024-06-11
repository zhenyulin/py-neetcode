from src.array_2d.search_shortest_spread import shortestSpread


def testShortestSpread():
    assert shortestSpread([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
    assert shortestSpread([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
    assert shortestSpread([[0, 2]]) == 0
