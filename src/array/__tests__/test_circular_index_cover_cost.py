from src.array.circular_index_cover_cost import canCompleteCircuit


def testCanCompleteCircuit():
    assert canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3
    assert canCompleteCircuit([2, 3, 4], [3, 4, 3]) == -1
