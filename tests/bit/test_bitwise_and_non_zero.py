from src.bit.bitwise_and_non_zero import maxSum


def testMaxSum():
    assert maxSum([1]) == 1
    assert maxSum([1, 2]) == 2
    assert maxSum([1, 3, 5, 9]) == 18
