from typing import Self, Iterator

from .hashmap import HashMap, Input


class Set:
    def __init__(self, elements: list[Input] = []) -> None:
        """time complexity: O(M)"""
        self.items = HashMap()
        for e in elements:
            self.items.put(e)

    def __len__(self):
        return self.items.__len__()

    def __contains__(self, e: Input) -> bool:
        """time complexity: O(1)"""
        return self.items.contains(e)

    contains = __contains__

    def __iter__(self) -> Iterator:
        return self.items.__iter__()

    def add(self, e: Input) -> None:
        """time complexity: O(1)"""
        self.items.put(e)

    # safe remove
    def remove(self, e: Input) -> None:
        """time complexity: O(1)"""
        try:
            self.items.remove(e)
        except KeyError:
            pass

    def union(self, target: Self) -> Self:
        """time complexity: O(M+N)"""
        return Set([*self.items, *target.items])

    def intersection(self, target: Self) -> Self:
        """time complexity: O(min(M, N))"""
        smaller, bigger = (self, target) if len(self) < len(target) else (target, self)
        res = Set([e for e in smaller if e in bigger])
        return res

    def diff(self, target: Self) -> Self:
        """time complexity: O(M)"""
        res = Set([e for e in self if e not in target])
        return res
