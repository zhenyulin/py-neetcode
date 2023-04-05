from src.array.except_self_product import productExceptSelf


def testProductExceptSelf():
    assert productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
