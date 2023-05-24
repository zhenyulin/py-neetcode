from unittest.mock import patch

from src.structure.rate_limiter import RateLimiter


def testRateLimiter():
    rl = RateLimiter()
    assert rl.accept() is True
    assert rl.accept() is True
    assert rl.accept() is True
    assert rl.accept() is False
