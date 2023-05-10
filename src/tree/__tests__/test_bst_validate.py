from src.tree.bst_validate import validateBST
from src.tree.tree_node import list_to_tree


def testValidateBST():
    tree = list_to_tree([2, 1, 3])
    assert validateBST(tree) is True
    tree = list_to_tree([5, 1, 4, None, None, 3, 6])
    assert validateBST(tree) is False
    tree = list_to_tree([])
    assert validateBST(tree) is True
