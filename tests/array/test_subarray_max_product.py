from src.array.subarray_max_product import maxProduct


def testMaxProduct():
    assert maxProduct([2, 3, -2, 4]) == 6
    assert maxProduct([-2, 0, -1]) == 0
