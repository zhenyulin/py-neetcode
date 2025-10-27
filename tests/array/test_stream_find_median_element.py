from tests.benchmark import benchmark_implementations

from rust.array import MedianFinder as RustMedianFinder
from src.array.stream_find_median_element import MedianFinder


def test_median_finder():
    stream = MedianFinder()
    stream.add_num(1)
    stream.add_num(2)
    assert stream.find_median() == 1.5
    stream.add_num(3)
    assert stream.find_median() == 2


@benchmark_implementations({"py": MedianFinder, "rs": RustMedianFinder})
def test_benchmark(benchmark, implementation):
    def run():
        stream = implementation()
        for i in range(1, 1000):
            stream.add_num(i)
        return stream.find_median()

    assert benchmark(run) == 500.0
