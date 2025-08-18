from collections.abc import Mapping

import pytest


def benchmark_implementations(implementations: Mapping[str, callable]):
    parametrize = pytest.mark.parametrize(
        ("implementation"), implementations.values(), ids=implementations.keys()
    )

    def decorator(func):
        return pytest.mark.benchmark(parametrize(func))

    return decorator
