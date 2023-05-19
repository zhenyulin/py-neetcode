#
# https://wiki.python.org/moin/TimeComplexity
#


from typing import Self, Iterator

from .hashmap import HashMap, Input


class Set:
    def __init__(self, elements: list[Input] = []) -> None:
        """time complexity: O(N)"""
        self.hashmap = HashMap()
        for e in elements:
            self.hashmap.put(e)

    def __len__(self):
        return self.hashmap.__len__()

    def __contains__(self, e: Input) -> bool:
        """
        average time complexity: O(1), assuming collisions are uncommon
        amortised time complexity: O(N), in case of collisions
        ~ hashmap.contains
        """
        return self.hashmap.contains(e)

    contains = __contains__

    def __iter__(self) -> Iterator:
        """time complexity: O(N)"""
        return self.hashmap.__iter__()

    def add(self, e: Input) -> None:
        """
        average time complexity: O(1), assuming collisions are uncommon
        amortised time complexity: O(N), in case of collisions
        """
        self.hashmap.put(e)

    def remove(self, e: Input) -> None:
        """safe remove

        average time complexity: O(1), assuming collisions are uncommon
        amortised time complexity: O(N), in case of collisions
        """
        try:
            self.hashmap.remove(e)
        except KeyError:
            pass

    def union(self, target: Self) -> Self:
        """time complexity: O(N+M)"""
        return Set([*self.hashmap, *target.hashmap])

    __or__ = union

    def intersection(self, target: Self) -> Self:
        """
        average time complexity: O(min(M, N)), assuming collisions are uncommon
        amortised time complexity: O(M*N), in case of collisions
        """
        smaller, bigger = (self, target) if len(self) < len(target) else (target, self)
        res = Set([e for e in smaller if e in bigger])
        return res

    __and__ = intersection

    def diff(self, target: Self) -> Self:
        """time complexity: O(N)"""
        res = Set([e for e in self if e not in target])
        return res

    __sub__ = diff
