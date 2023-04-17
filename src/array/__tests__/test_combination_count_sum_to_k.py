from src.array.combination_count_sum_to_k import waysOfChange


def testWaysOfChange():
    assert waysOfChange([1, 2, 5], 5) == 4
    assert waysOfChange([2], 3) == 0
    assert waysOfChange([10], 10) == 1
