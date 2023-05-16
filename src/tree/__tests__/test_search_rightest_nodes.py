from src.tree.search_rightest_nodes import rightSideView


def testRighSideView():
    assert rightSideView([1, 2, 3, None, 5, None, 4]) == [1, 3, 4]
    assert rightSideView([1, None, 3]) == [1, 3]
    assert rightSideView([]) == []
