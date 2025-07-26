from src.array.combination_fewest_elements_sum_to import fewest_elements_sum


def test_fewest_elements_sum():
    assert fewest_elements_sum([1, 2, 5], 11) == 3
    assert fewest_elements_sum([2], 3) == -1
    assert fewest_elements_sum([1], 0) == 0
