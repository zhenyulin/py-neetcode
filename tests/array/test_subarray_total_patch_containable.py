from tests.benchmark import benchmark_implementations

from rust.array import total_patch as rust_total_patch
from src.array.subarray_total_patch_containable import total_patch


def test_total_patch():
    assert total_patch([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert total_patch([4, 2, 0, 3, 2, 5]) == 9


@benchmark_implementations({"py": total_patch, "rs": rust_total_patch})
def test_benchmark(benchmark, implementation):
    heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    assert benchmark(implementation, heights) == 6
