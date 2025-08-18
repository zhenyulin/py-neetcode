from tests.benchmark import benchmark_implementations

from rust.string import generate_parentheses as generate_parentheses_rust
from src.string.combination_generate_parentheses import generate_parentheses


def test_generate_parentheses():
    assert set(generate_parentheses(3)) == {"((()))", "(()())", "(())()", "()(())", "()()()"}
    assert generate_parentheses(1) == ["()"]


IMPLEMENTATIONS = {"py": generate_parentheses, "rs": generate_parentheses_rust}


@benchmark_implementations(IMPLEMENTATIONS)
def test_benchmark(benchmark, implementation):
    result = benchmark(implementation, 3)
    assert set(result) == {"((()))", "(()())", "(())()", "()(())", "()()()"}
