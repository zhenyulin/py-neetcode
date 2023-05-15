from src.linked_list.list_node import to_linked_list, to_list

from src.linked_list.reorder_from_midpoint import reorderList


def testReorderList():
    assert to_list(
        reorderList(
            to_linked_list(
                [1, 2, 3, 4],
            )
        )
    ) == [1, 4, 2, 3]
