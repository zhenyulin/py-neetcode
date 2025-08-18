from tests.benchmark import benchmark_implementations

from rust.array import min_sub_array_len as rust_min_sub_array_len
from src.array.subarray_min_size_sum import min_sub_array_len


def test_min_sub_array_len():
    assert min_sub_array_len(7, [2, 3, 1, 2, 4, 3]) == 2
    assert min_sub_array_len(4, [1, 4, 4]) == 1
    assert min_sub_array_len(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0


@benchmark_implementations({"py": min_sub_array_len, "rust": rust_min_sub_array_len})
def test_benchmark(benchmark, implementation):
    result = benchmark(implementation, 7, [2, 3, 1, 2, 4, 3])
    assert result == 2, f"Expected 2, got {result}"
