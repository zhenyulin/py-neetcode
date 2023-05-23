from src.graph.detect_cycle import canFinish


def testCanFinish():
    assert canFinish(2, [[1, 0]]) is True
    assert canFinish(2, [[1, 0], [0, 1]]) is False
