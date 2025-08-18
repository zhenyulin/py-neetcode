from tests.benchmark import benchmark_implementations

from rust.string import longest_common_subsequence as longest_common_subsequence_rust
from src.string.subsequence_count_longest_common_two_strings import (
    longest_common_subsequence,
)


def test_longest_common_subsequence():
    assert longest_common_subsequence("abcde", "ace") == 3
    assert longest_common_subsequence("abc", "abc") == 3
    assert longest_common_subsequence("abc", "def") == 0


IMPLEMENTATIONS = {"py": longest_common_subsequence, "rs": longest_common_subsequence_rust}


@benchmark_implementations(IMPLEMENTATIONS)
def test_benchmark(benchmark, implementation):
    benchmark(implementation, "abcde", "ace")
