from typing import Optional

from .hashmap import Input


class PriorityCache:
    """
    a priority cache that can
    - sort cache by priority
    - get value by key
    - add new key value, pop low priority one if full
    - update value by key
    - update priority by key

    1) Dict & Sorted Linked List

    dict: {key: Linked List Node}
    linked_list: [(key, value, priority)]

    get: O(1), pop: O(1), add: O(N), update_value: O(1), update_priority: O(N)

    2) Dict & Sorted List

    dict: {key: value}
    list: [(key, priority)]

    get: O(1), pop: O(1), add: O(N), update_value: O(1), update_priority: O(N)

    3) Dict & Heap

    dict: {key: value, timestamp}
    heap: [(priority, timestamp, key)]

    get: O(1), pop: O(logN), add: O(logN), update_value: O(1), update_priority: O(logN)
    """

    def __init__(self, capacity=10) -> None:
        self.capacity = capacity
        self.cache = {}
        self.priority = []

    def get(self, key: Input) -> any:
        """
        cache {key: value}

        time complexity: O(1)
        """
        return self.cache[key]

    def pop(self) -> any:
        """
        pop the job of the highest priority

        time complexity: O(1)
        """
        _, key = self.priority.pop()
        val = self.cache[key]
        del self.cache[key]
        return val

    def add(self, key: Input, value: any, priority: int) -> None:
        """
        amortised time complexity: O(N)
        """
        if len(self.priority) == self.capacity:
            self.pop()
        self.priority.append((priority, key))
        self.priority.sort(key=lambda x: x[0], reverse=True)
        self.cache[key] = value

    def update_value(self, key: Input, value: any) -> None:
        """
        time complexity: O(1)
        """
        if key not in self.cache:
            raise KeyError("key not found")

        self.cache[key] = value

    def update_priority(self, key: Input, priority: int) -> None:
        """
        amortised time complexity: O(N)
        """
        if key not in self.cache:
            raise KeyError("key not found")

        self.priority = [(p, k) for p, k in self.priority if k != key] + [
            (priority, key)
        ]
        self.priority.sort(key=lambda x: x[0], reverse=True)
