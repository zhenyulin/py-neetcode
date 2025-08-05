import pytest

from rust.string import longest_common_subsequence as longest_common_subsequence_rust
from src.string.subsequence_count_longest_common_two_strings import (
    longest_common_subsequence,
)


def test_longest_common_subsequence():
    assert longest_common_subsequence("abcde", "ace") == 3
    assert longest_common_subsequence("abc", "abc") == 3
    assert longest_common_subsequence("abc", "def") == 0


IMPLEMENTATIONS = {"py": longest_common_subsequence, "rs": longest_common_subsequence_rust}


@pytest.mark.benchmark
@pytest.mark.parametrize(("implementation"), IMPLEMENTATIONS.values(), ids=IMPLEMENTATIONS.keys())
def test_benchmark(benchmark, implementation):
    benchmark(implementation, "abcde", "ace")
