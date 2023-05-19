#
# https://wiki.python.org/moin/TimeComplexity
#
# Common Collision Policies:
# [x] Separate bucketing
# [ ] Open Addressing: store in the next available empty slot in the array
# can be implemented using linear probing or quadratic probing or [double hash]
# [ ] Robinhood Hashing: add to the index, reorganise the bucket for ideal index
#


from typing import Iterator

Input = int | float | str | tuple


class HashMap:
    def __init__(self, capacity: int = 10) -> None:
        """
        to minimise memory needed for the list on initialisation
        a capacity is used to allocate bucket for hash keys

        time complexity: O(1)
        """
        self.capacity = capacity
        self.buckets = [[] for _ in range(self.capacity)]
        self.length = 0

    def _hash_key(self, key: Input) -> int:
        """time complexity: O(1)"""
        return hash(key) % self.capacity

    def __len__(self) -> int:
        """time complexity: O(1)"""
        return self.length

    def __contains__(self, key: Input) -> bool:
        """
        average time complexity: O(1), assuming collisions are uncommon
        amortised time complexity: O(N), in case of collisions
        """
        index = self._hash_key(key)
        for k, _ in self.buckets[index]:
            if k == key:
                return True
        return False

    def __iter__(self) -> Iterator:
        """time complexity: O(N)"""
        for bucket in self.buckets:
            for key, _ in bucket:
                yield key

    def __getitem__(self, key: Input) -> any:
        """
        average time complexity: O(1), assuming collisions are uncommon
        amortised time complexity: O(N), in case of collisions
        """
        index = self._hash_key(key)
        for k, v in self.buckets[index]:
            if k == key:
                return v
        raise KeyError(f"{key} not found")

    def __setitem__(self, key: Input, value: any = None) -> None:
        """
        average time complexity: O(1), assuming collisions are uncommon
        amortised time complexity: O(N), in case of collisions
        """
        index = self._hash_key(key)
        for entry in self.buckets[index]:
            if entry[0] == key:
                entry[1] = value
                return
        self.buckets[index].append([key, value])
        self.length += 1

    def __delitem__(self, key: Input) -> None:
        """
        average time complexity: O(1), assuming collisions are uncommon
        amortised time complexity: O(N), in case of collisions
        """
        index = self._hash_key(key)
        for i, (k, _) in enumerate(self.buckets[index]):
            if k == key:
                del self.buckets[index][i]
                self.length -= 1
                return
        raise KeyError(f"{key} not found")

    contains = __contains__
    get = __getitem__
    put = __setitem__
    remove = __delitem__

    def keys(self) -> list[Input]:
        """time complexity: O(N)"""
        keys = []
        for bucket in self.buckets:
            for k, _ in bucket:
                keys.append(k)
        return keys

    def values(self) -> list[any]:
        """time complexity: O(N)"""
        values = []
        for bucket in self.buckets:
            for _, v in bucket:
                values.append(v)
        return values

    def items(self) -> list[tuple[Input, any]]:
        """time complexity: O(N)"""
        items = []
        for bucket in self.buckets:
            for pair in bucket:
                items.append(tuple(pair))
        return items
