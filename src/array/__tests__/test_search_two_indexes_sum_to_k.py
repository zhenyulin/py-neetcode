from src.array.search_two_indexes_sum_to_k import twoSum


def test_two_sum():
    # the problem has been constrained to have only one valid answer
    assert twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert twoSum([3, 2, 4], 6) == [1, 2]
    assert twoSum([3, 3], 6) == [0, 1]
