from tests.benchmark import benchmark_implementations

from rust.array import max_product as rust_max_product
from src.array.subarray_max_product import max_product


def test_max_product():
    assert max_product([2, 3, -2, 4]) == 6
    assert max_product([-2, 0, -1]) == 0


IMPLEMENTATIONS = {
    "py": max_product,
    "rs": rust_max_product,
}


@benchmark_implementations(IMPLEMENTATIONS)
def test_max_product_benchmark(benchmark, implementation):
    result = benchmark(implementation, [2, 3, -2, 4])
    assert result == 6
