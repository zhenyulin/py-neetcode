import pytest

from rust.string import length_of_longest_substring as length_of_longest_substring_rust
from src.string.substring_longest_without_repeating_characters import (
    length_of_longest_substring,
)


def test_length_of_longest_substring():
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("pwwkew") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("") == 0


IMPLEMENTATIONS = {
    "py": length_of_longest_substring,
    "rs": length_of_longest_substring_rust,
}


@pytest.mark.benchmark
@pytest.mark.parametrize(("implementation"), IMPLEMENTATIONS.values(), ids=IMPLEMENTATIONS.keys())
def test_benchmark_length_of_longest_substring(benchmark, implementation):
    """Benchmark the length_of_longest_substring implementations."""
    data = "abcabcbb" * 1000
    benchmark(implementation, data)
