from src.array.triplet_check_increasing import increasingTriplet


def testIncreasingTriplet():

    assert increasingTriplet([1, 2, 3, 4, 5]) == True
    assert increasingTriplet([5, 4, 3, 2, 1]) == False
    assert increasingTriplet([2, 1, 5, 0, 4, 6]) == True
    assert increasingTriplet([2, 3, 2, 1, 6]) == True
