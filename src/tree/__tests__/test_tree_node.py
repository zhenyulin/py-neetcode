from src.tree.tree_node import TreeNode, tree_to_list, list_to_tree


def testTreeToList():
    assert tree_to_list(None) is None

    tree = TreeNode(None)

    assert tree
    assert tree_to_list(tree) == [None]

    tree = TreeNode(0, left=TreeNode(1), right=TreeNode(2))

    assert tree_to_list(tree) == [0, 1, 2]

    tree.left.right = TreeNode(3)

    assert tree_to_list(tree) == [0, 1, 2, None, 3]


def testListToTree():

    assert list_to_tree([]) is None

    tree = list_to_tree([None])
    assert tree and tree.val is None

    tree = list_to_tree([1, None, 2])
    assert tree and tree.val == 1
    assert tree.left is None and tree.right.val == 2

    tree = list_to_tree([1, None, 0])
    assert tree and tree.val == 1
    assert tree.left is None and tree.right.val == 0

    tree = list_to_tree([0, 1, 2, None, 3])
    assert tree_to_list(tree) == [0, 1, 2, None, 3]

    tree = list_to_tree([1, 2, 3, None, 5, None, 4])
    assert tree_to_list(tree) == [1, 2, 3, None, 5, None, 4]
