from src.linked_list.reorder_from_midpoint import reorderList


def testReorderList():
    assert reorderList([1, 2, 3, 4]) == [1, 4, 2, 3]
