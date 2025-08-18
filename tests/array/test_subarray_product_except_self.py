from tests.benchmark import benchmark_implementations

from rust import array
from src.array.subarray_product_except_self import product_except_self


def test_product_except_self():
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]


@benchmark_implementations({"py": product_except_self, "rs": array.product_except_self})
def test_benchmark(benchmark, implementation):
    assert benchmark(implementation, [1, 2, 3, 4]) == [24, 12, 8, 6]
