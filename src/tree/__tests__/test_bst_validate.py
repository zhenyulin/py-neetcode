from src.tree.bst_validate import validateBST


def testValidateBST():
    assert validateBST([2, 1, 3]) is True
    assert validateBST([5, 1, 4, None, None, 3, 6]) is False
    assert validateBST([]) is True
