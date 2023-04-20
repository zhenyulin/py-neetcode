from src.array.subarray_count_sum_divisible_by_k import subarrayDivByK


def testSubarrayDivByK():

    assert subarrayDivByK([4, 5, 0, -2, -3, 1], 5) == 7
    assert subarrayDivByK([5], 9) == 0
