from src.graph.undirected_remove_cycle import removeCycle


def testRemoveCycle():
    assert removeCycle([[1, 2], [1, 3], [2, 3]]) == [2, 3]
    assert removeCycle([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]) == [1, 4]
