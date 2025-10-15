from tests.benchmark import benchmark_implementations

from rust.array import largest_area_rectangle as largest_area_rectangle_rust
from src.array.subarray_max_area_rectangle import largest_area_rectangle


def test_largest_area_rectangle():
    assert largest_area_rectangle([2, 1, 5, 6, 2, 3]) == 10
    assert largest_area_rectangle([2, 4]) == 4


@benchmark_implementations({"py": largest_area_rectangle, "rs": largest_area_rectangle_rust})
def test_benchmark(benchmark, implementation):
    assert benchmark(implementation, [2, 1, 5, 6, 2, 3]) == 10
