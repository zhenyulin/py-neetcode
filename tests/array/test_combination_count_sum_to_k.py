from src.array.combination_count_sum_to_k import ways_of_change


def test_ways_of_change():
    """Test cases for ways_of_change function."""
    assert ways_of_change([1, 2, 5], 5) == 4
    assert ways_of_change([2], 3) == 0
    assert ways_of_change([10], 10) == 1
