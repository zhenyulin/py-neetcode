from src.tree.search_rightmost_nodes import right_side_view


def test_right_side_view():
    """Test for right_side_view function."""
    assert right_side_view([1, 2, 3, None, 5, None, 4]) == [1, 3, 4]
    assert right_side_view([1, None, 3]) == [1, 3]
    assert right_side_view([]) == []
