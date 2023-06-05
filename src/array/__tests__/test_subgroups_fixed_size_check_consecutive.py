from src.array.subgroups_fixed_size_check_consecutive import canBeGrouped


def testCanBeGrouped():
    assert canBeGrouped([1, 2, 3, 6, 2, 3, 4, 7, 8], 3) is True
    assert canBeGrouped([3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11], 3) is True
    assert canBeGrouped([1, 2, 3, 4], 3) is False
