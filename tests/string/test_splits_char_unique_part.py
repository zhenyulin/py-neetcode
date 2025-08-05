import pytest

from rust.string import partition_lengths as partition_lengths_rust
from src.string.splits_char_unique_part import partition_lengths


def test_partition_lengths():
    assert partition_lengths("ababcbacadefegdehijhklij") == [9, 7, 8]
    assert partition_lengths("eccbbbbdec") == [10]


IMPLEMENTATIONS = {"py": partition_lengths, "rs": partition_lengths_rust}


@pytest.mark.benchmark
@pytest.mark.parametrize(("implementation"), IMPLEMENTATIONS.values(), ids=IMPLEMENTATIONS.keys())
def test_benchmark(benchmark, implementation):
    result = benchmark(implementation, "ababcbacadefegdehijhklij")
    assert result == [9, 7, 8]
