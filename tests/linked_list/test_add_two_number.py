from src.linked_list.add_two_number import addTwoNumber


def testAddTwoNumber():
    assert addTwoNumber([0], [0]) == [0]
    assert addTwoNumber([2, 4, 3], [5, 6, 4]) == [7, 0, 8]
    assert addTwoNumber([9, 9, 9], [1]) == [0, 0, 0, 1]
