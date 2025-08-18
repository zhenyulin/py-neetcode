from tests.benchmark import benchmark_implementations

from rust.string import char_replacement as char_replacement_rust
from src.string.substring_longest_char_replacement import char_replacement


def test_char_replacement():
    assert char_replacement("ABAB", 2) == 4
    assert char_replacement("AABABBA", 1) == 4


IMPLEMENTATIONS = {
    "py": char_replacement,
    "rs": char_replacement_rust,
}


@benchmark_implementations(IMPLEMENTATIONS)
def test_benchmark_char_replacement(benchmark, implementation):
    """Benchmark the char_replacement implementations."""
    data = "AACABBA" * 1000
    benchmark(implementation, data, 3)
