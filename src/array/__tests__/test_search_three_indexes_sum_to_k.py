from src.array.search_three_indexes_sum_to_k import threeSum


def testThreeSum():

    assert threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, 0, 1], [-1, -1, 2]]
    assert threeSum([0, 1, 1]) == []
    assert threeSum([0, 0, 0]) == [[0, 0, 0]]
