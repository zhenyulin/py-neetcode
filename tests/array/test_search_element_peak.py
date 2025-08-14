import pytest

from rust.array import find_peak_element as find_peak_element_rust
from src.array.search_element_peak import find_peak_element


def test_find_peak_element():
    assert find_peak_element([1, 2, 3, 1]) == 2
    assert find_peak_element([1, 2, 1, 3, 5, 6, 4]) == 5


IMPLEMENTATIONS = {"py": find_peak_element, "rs": find_peak_element_rust}


@pytest.mark.benchmark
@pytest.mark.parametrize(("implementation"), IMPLEMENTATIONS.values(), ids=IMPLEMENTATIONS.keys())
def test_benchmark(benchmark, implementation):
    result = benchmark(implementation, [1, 2, 3, 1])
    assert result == 2
