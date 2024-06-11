#
# Check Whether a Given Point is within a Triangle
# https://www.geeksforgeeks.org/check-whether-a-given-point-lies-inside-a-triangle-or-not/amp/
#
Coordinates = tuple[int, int]


def isInside(a: Coordinates, b: Coordinates, c: Coordinates, p: Coordinates) -> bool:
    """1) we can check whether the total areas of the three triangles formed from 'p'
    equals the one of 'abc'.

    time complexity: O(1), space complexity: O(1)
    """

    def area(a: Coordinates, b: Coordinates, c: Coordinates) -> float:
        (x1, y1), (x2, y2), (x3, y3) = a, b, c
        return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2

    return area(a, b, c) == area(a, b, p) + area(a, c, p) + area(b, c, p)
