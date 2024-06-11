from src.geometry.point_check_in_triangle import isInside


def testIsInside():
    assert isInside((0, 0), (10, 30), (20, 0), (10, 15)) == True
    assert isInside((0, 0), (10, 30), (20, 0), (30, 15)) == False
