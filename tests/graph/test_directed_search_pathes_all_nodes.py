from src.graph.directed_search_pathes_all_nodes import findPathes


def testFindPathes():
    assert findPathes(2, [[1, 0]]) == [0, 1]
    assert findPathes(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) == [0, 1, 2, 3]
    assert findPathes(1, []) == [0]
    assert findPathes(2, [[1, 0], [0, 1]]) == []
