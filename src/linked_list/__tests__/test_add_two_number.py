from src.linked_list.list_node import to_linked_list, to_list

from src.linked_list.add_two_number import addTwoNumber


def testAddTwoNumber():
    assert to_list(
        addTwoNumber(
            to_linked_list([0]),
            to_linked_list([0]),
        )
    ) == [0]

    assert to_list(
        addTwoNumber(
            to_linked_list([2, 4, 3]),
            to_linked_list([5, 6, 4]),
        )
    ) == [7, 0, 8]

    assert to_list(
        addTwoNumber(
            to_linked_list([9, 9, 9]),
            to_linked_list([1]),
        )
    ) == [0, 0, 0, 1]
