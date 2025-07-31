import pytest

from rust.string import num_splits as num_split_rust
from src.string.splits_count_equal_unique_chars import num_split


def test_num_split():
    assert num_split("a") == 0
    assert num_split("aa") == 1
    assert num_split("ab") == 1
    assert num_split("abcd") == 1
    assert num_split("aacaba") == 2


def test_num_split_rust():
    assert num_split_rust("a") == 0
    assert num_split_rust("aa") == 1
    assert num_split_rust("ab") == 1
    assert num_split_rust("abcd") == 1
    assert num_split_rust("aacaba") == 2


IMPLEMENTATIONS = {"rs": num_split_rust, "py": num_split}


@pytest.mark.benchmark
@pytest.mark.parametrize("implementation", IMPLEMENTATIONS.values(), ids=IMPLEMENTATIONS.keys())
def test_benchmark(benchmark, implementation):
    benchmark(implementation, "aacaba" * 1000)
