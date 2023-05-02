from typing import Self

Input = int | float | str | tuple


class Set:
    def __init__(self, elements: list[Input] = []) -> None:
        """time complexity: O(M)"""
        self.items = {e: True for e in elements}

    def contains(self, e: Input) -> bool:
        """time complexity: O(1)"""
        return e in self.items

    def add(self, e: Input) -> None:
        """time complexity: O(1)"""
        self.items[e] = True

    # safe remove
    def remove(self, e: Input) -> None:
        """time complexity: O(1)"""
        self.items.pop(e, None)

    def union(self, target: Self) -> Self:
        """time complexity: O(M+N)"""
        res = Set()
        res.items = {**self.items, **target.items}
        return res

    def intersection(self, target: Self) -> Self:
        """time complexity: O(min(M, N))"""
        smaller, bigger = (
            (self.items, target.items)
            if len(self.items) < len(target.items)
            else (target.items, self.items)
        )
        res = Set([e for e in smaller if e in bigger])
        return res

    def diff(self, target: Self) -> Self:
        """time complexity: O(M)"""
        res = Set([e for e in self.items if not target.contains(e)])
        return res
