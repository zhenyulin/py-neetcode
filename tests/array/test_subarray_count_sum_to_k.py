from src.array.subarray_count_sum_to_k import subarraySum


def testSubarraySum():
    assert subarraySum([1, 1, 1], 0) == 0
    assert subarraySum([1, 1, 1], 2) == 2
    assert subarraySum([1, 2, 3], 3) == 2
