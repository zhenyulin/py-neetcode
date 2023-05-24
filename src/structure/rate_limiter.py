from collections import deque
from time import time


class RateLimiter:
    """
    1) deque stack:

    accept: O(1)
    """

    def __init__(self, window_size: int = 1, rate_limit: int = 3):
        self.window = deque()
        self.window_size = window_size
        self.rate_limit = rate_limit

    def accept(self):
        now = time()
        while self.window and self.window[0] < now - self.window_size:
            self.window.popleft()

        if len(self.window) >= self.rate_limit:
            return False

        self.window.append(now)

        return True
