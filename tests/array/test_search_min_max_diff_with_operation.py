from tests.benchmark import benchmark_implementations

from rust.array import smallest_range as rust_smallest_range
from src.array.search_min_max_diff_with_operation import smallest_range


def test_smallest_range():
    assert smallest_range([1], 0) == 0
    assert smallest_range([0, 10], 2) == 6
    assert smallest_range([1, 3, 6], 3) == 3
    assert smallest_range([2, 7, 2], 1) == 3
    assert smallest_range([3, 1, 10], 4) == 2


@benchmark_implementations({"py": smallest_range, "rust": rust_smallest_range})
def test_benchmark_smallest_range(benchmark, implementation):
    result = benchmark(implementation, [1, 3, 6], 3)
    assert result == 3
