from src.array.subarray_total_patch_containable import totalPatch


def testTotalPatch():
    assert totalPatch([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert totalPatch([4, 2, 0, 3, 2, 5]) == 9
