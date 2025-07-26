from src.array.circular_index_cover_cost import can_complete_circuit


def test_can_complete_circuit():
    """Test cases for can_complete_circuit function."""
    assert can_complete_circuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3
    assert can_complete_circuit([2, 3, 4], [3, 4, 3]) == -1
