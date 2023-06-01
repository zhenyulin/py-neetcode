from src.array.subsequence_min_jumps import minJump


def testMinJump():
    assert minJump([2, 3, 1, 1, 4]) == 2
    assert minJump([2, 3, 0, 1, 4]) == 2
