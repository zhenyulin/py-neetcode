Input = int | float | str | tuple


class HashMap:
    def __init__(self, capacity: int = 10) -> None:
        """
        to minimise memory needed for the list on initialisation
        a capacity is used to allocate bucket for hash keys

        time complexity: O(1)
        """
        self.capacity = capacity
        self.map = [[] for _ in range(self.capacity)]
        self.length = 0

    def __len__(self):
        """time complexity: O(1)"""
        return self.length

    def __contains__(self, key: Input) -> bool:
        """time complexity: O(1)"""
        index = self._get_index(key)
        for k, _ in self.map[index]:
            if k == key:
                return True
        return False

    def __iter__(self):
        """time complexity: O(1)"""
        for chain in self.map:
            for key, _ in chain:
                yield key

    def __getitem__(self, key: Input) -> any:
        """time complexity: O(N)
        average time complexity: O(1) if there isn't many hash value collisions
        """
        index = self._get_index(key)
        for k, v in self.map[index]:
            if k == key:
                return v
        raise KeyError(f"{key} not found")

    def __setitem__(self, key: Input, value: any = None) -> None:
        """time complexity: O(N)
        average time complexity: O(1) if there isn't many hash value collisions

        common collision policies:
        - Separate Chaining [used here]
        - Open Addressing: store in the next available empty slot in the array
        can be implemented using linear probing or quadratic probing or double hash
        - Robinhood Hashing: add to the index, reorganise the bucket for ideal index
        """
        index = self._get_index(key)
        for pair in self.map[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.map[index].append([key, value])
        self.length += 1

    def __delitem__(self, key: Input) -> None:
        """time complexity: O(N)
        average time complexity: O(1) if there isn't many hash value collisions
        """
        index = self._get_index(key)
        for i, (k, _) in enumerate(self.map[index]):
            if k == key:
                del self.map[index][i]
                self.length -= 1
                return
        raise KeyError(f"{key} not found")

    contains = __contains__
    get = __getitem__
    put = __setitem__
    remove = __delitem__

    def _get_index(self, key: Input) -> int:
        """time complexity: O(1)"""
        return hash(key) % self.capacity

    def keys(self) -> list[Input]:
        """time complexity: O(N)"""
        keys = []
        for chain in self.map:
            for k, _ in chain:
                keys.append(k)
        return keys

    def values(self) -> list[any]:
        """time complexity: O(N)"""
        values = []
        for chain in self.map:
            for _, v in chain:
                values.append(v)
        return values

    def items(self) -> list[tuple[Input, any]]:
        """time complexity: O(N)"""
        items = []
        for chain in self.map:
            for pair in chain:
                items.append(tuple(pair))
        return items
