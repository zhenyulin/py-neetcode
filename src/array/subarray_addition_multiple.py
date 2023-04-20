#
# 370. Range Addition
# https://baihuqian.github.io/2018-08-16-range-addition/
#


def rangeAddition(length: int, operations: list[list[int, int, int]]) -> list[int]:
    """
    to do multiple addition to ranges lazily, we can utilise rolling addition

    1) Rolling Addition Greedy
    we can mark the start of the range with an addition,
    which can be rolling added to the end
    and next to the end a deduction,
    so that from this point on the previous addition would be ended

    time complexity: O(K+N), space complexity: O(1)
    """

    # make an extra space to denote deduction
    res = [0] * (length + 1)

    for [i, j, v] in operations:
        res[i] += v
        res[j + 1] -= v

    for i in range(1, length):
        res[i] += res[i - 1]

    return res[:-1]
