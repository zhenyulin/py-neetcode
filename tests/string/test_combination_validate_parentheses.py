from tests.benchmark import benchmark_implementations

from rust.string import validate_parenthesis as rust_validate_parenthesis
from src.string.combination_validate_parentheses import validate_parenthesis


def test_validate_parenthesis():
    assert validate_parenthesis("()") is True
    assert validate_parenthesis("(*)") is True
    assert validate_parenthesis("((*") is False
    assert validate_parenthesis("(*)))") is False
    assert validate_parenthesis("(*))") is True


def test_rust_validate_parenthesis():
    assert rust_validate_parenthesis("()") is True
    assert rust_validate_parenthesis("(*)") is True
    assert rust_validate_parenthesis("((*") is False
    assert rust_validate_parenthesis("(*)))") is False
    assert rust_validate_parenthesis("(*))") is True


IMPLEMENTATIONS = {
    "py": validate_parenthesis,
    "rs": rust_validate_parenthesis,
}


@benchmark_implementations(IMPLEMENTATIONS)
def test_benchmark(benchmark, implementation):
    # Benchmark the implementation
    benchmark(implementation, "(*))" * 100)
