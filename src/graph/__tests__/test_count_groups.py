from src.graph.count_groups import countGroups


def testCountGroups():
    assert countGroups([[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2
    assert countGroups([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3
