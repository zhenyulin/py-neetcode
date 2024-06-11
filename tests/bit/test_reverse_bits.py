from src.bit.reverse_bits import reverseBits


def testReverseBits():
    assert reverseBits(43261596) == 964176192
    assert reverseBits(4294967293) == 3221225471
