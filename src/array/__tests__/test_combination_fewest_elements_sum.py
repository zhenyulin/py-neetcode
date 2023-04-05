from src.array.combination_fewest_elements_sum import fewestElementsSum


def testFewestElementsSum():
    assert fewestElementsSum([1, 2, 5], 11) == 3
    assert fewestElementsSum([2], 3) == -1
    assert fewestElementsSum([1], 0) == 0
