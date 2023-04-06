from src.tree.tree_node import list_to_tree
from src.tree.search_rightest_nodes import rightSideView


def testRighSideView():

    tree = list_to_tree([1, 2, 3, None, 5, None, 4])
    assert rightSideView(tree) == [1, 3, 4]

    tree = list_to_tree([1, None, 3])
    assert rightSideView(tree) == [1, 3]

    tree = list_to_tree([])
    assert rightSideView(tree) == []
