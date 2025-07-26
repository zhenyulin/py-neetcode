from src.linked_list.add_two_number import add_two_numbers


def test_add_two_numbers():
    assert add_two_numbers([0], [0]) == [0]
    assert add_two_numbers([2, 4, 3], [5, 6, 4]) == [7, 0, 8]
    assert add_two_numbers([9, 9, 9], [1]) == [0, 0, 0, 1]
