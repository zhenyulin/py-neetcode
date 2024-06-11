from collections import defaultdict

from .hashmap import Input


class LFUCache:
    """1) dict & count dict
    use a dict as cache, and a dict to record the count.

    get: O(1), put: O(N)

    2) dict & count heap
    dict: {key: value, timestamp}
    heap: [(count, timestamp, key)]

    get: O(logN), put: O(logN)
    """

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache = {}
        self.count = defaultdict(int)

    def get(self, key: Input) -> any:
        """Time complexity: O(1)."""
        if key not in self.cache:
            return None

        self.count[key] += 1
        return self.cache[key]

    def put(self, key: Input, value: any) -> None:
        """Time complexity: O(N)."""
        if key not in self.cache and len(self.cache) == self.capacity:
            expired_key = min(self.count, key=self.count.get)
            del self.cache[expired_key]
            del self.count[expired_key]

        self.cache[key] = value
        self.count[key] = 1
