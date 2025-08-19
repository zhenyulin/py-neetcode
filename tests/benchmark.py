from collections.abc import Callable, Mapping

import pytest


def benchmark_implementations(implementations: Mapping[str, Callable]) -> Callable:
    parametrize = pytest.mark.parametrize(
        ("implementation"), implementations.values(), ids=implementations.keys()
    )

    def decorator(func):
        return pytest.mark.benchmark(parametrize(func))

    return decorator
