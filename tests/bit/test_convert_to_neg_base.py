from src.bit.convert_to_neg_base import negBase


def testNegBase():
    assert negBase(0) == "0"
    assert negBase(2) == "110"
    assert negBase(3) == "111"
    assert negBase(4) == "100"
