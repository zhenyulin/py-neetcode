import pytest
from pytest_unordered import unordered

from cy.string.group_by_anagram import group_anagrams_26lower as group_anagrams_cython
from rust.string import group_anagrams as group_anagrams_rust
from src.string.group_by_anagram import group_anagrams

BASE = ["eat", "tea", "tan", "ate", "nat", "bat"]

IMPLEMENTATIONS = {
    "py": group_anagrams,
    "cy": group_anagrams_cython,
    "rs": group_anagrams_rust,
}


def expected_groups(multiplier: int) -> list[list[str]]:
    """Expected results."""
    return [
        ["bat"] * multiplier,
        ["nat", "tan"] * multiplier,
        ["ate", "eat", "tea"] * multiplier,
    ]


def unordered_2d(list_of_lists):
    """Mark both dimensions as order-insensitive."""
    return unordered([unordered(g) for g in list_of_lists])


@pytest.mark.parametrize(("implementation"), IMPLEMENTATIONS.values(), ids=IMPLEMENTATIONS.keys())
@pytest.mark.parametrize("multiplier", [100, 1000], ids=lambda m: f"{m}x")
def test_group_anagrams_benchmark(benchmark, implementation, multiplier):
    """Benchmark the group_anagrams implementations."""
    benchmark.group = multiplier

    data = BASE * multiplier
    result = benchmark(implementation, data)

    assert result == unordered_2d(expected_groups(multiplier))
