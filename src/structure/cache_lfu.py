from collections import defaultdict

from .hashmap import Input


class LFUCache:
    def __init__(self, capacity: int) -> None:
        """
        use a dict as cache, and a dict to record the count
        plus use a min heap to optimise the sorting at push time

        time complexity: O(1)
        """
        self.capacity = capacity
        self.cache = {}
        self.count = defaultdict(int)

    def get(self, key: Input) -> any:
        """time complexity: O(1)"""
        if key not in self.cache:
            return None

        self.count[key] += 1
        return self.cache[key]

    def put(self, key: Input, value: any) -> None:
        """time complexity: O(NLogN)"""

        if key not in self.cache and len(self.cache) == self.capacity:
            expired_key = min(self.count, key=self.count.get)
            del self.cache[expired_key]
            del self.count[expired_key]

        self.cache[key] = value
        self.count[key] = 1
