from tests.benchmark import benchmark_implementations

from rust.string import num_ways as rust_num_ways
from src.string.splits_count_equal_num_char import num_ways


def test_num_ways():
    assert num_ways("10101") == 4
    assert num_ways("1001") == 0
    assert num_ways("0000") == 3


def test_rust_num_ways():
    assert rust_num_ways("10101") == 4
    assert rust_num_ways("1001") == 0
    assert rust_num_ways("0000") == 3


IMPLEMENTATIONS = {
    "py": num_ways,
    "rs": rust_num_ways,
}


@benchmark_implementations(IMPLEMENTATIONS)
def test_num_ways_benchmark(benchmark, implementation):
    """Benchmark the num_ways implementations."""
    benchmark(implementation, "10101" * 100)
