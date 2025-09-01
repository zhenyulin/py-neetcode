from tests.benchmark import benchmark_implementations

from rust.array import find_shortest_subarray_to_remove as rust_impl
from src.array.subarray_shortest_remove_to_sort import find_shortest_subarray_to_remove


def test_find_shortest_subarray_to_remove():
    assert find_shortest_subarray_to_remove([1, 2, 3, 10, 4, 2, 3, 5]) == 3
    assert find_shortest_subarray_to_remove([5, 4, 3, 2, 1]) == 4
    assert find_shortest_subarray_to_remove([1, 2, 3]) == 0


@benchmark_implementations({"py": find_shortest_subarray_to_remove, "rs": rust_impl})
def test_benchmark(benchmark, implementation):
    assert benchmark(implementation, [1, 2, 3, 10, 4, 2, 3, 5]) == 3
