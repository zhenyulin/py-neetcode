from src.array.search_element_peak import findPeakElement


def testFindPeakElement():
    assert findPeakElement([1, 2, 3, 1]) == 2
    assert findPeakElement([1, 2, 1, 3, 5, 6, 4]) == 5
