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

    def _get_index(self, key: Input) -> int:
        """time complexity: O(1)"""
        return hash(key) % self.capacity

    def put(self, key: Input, value: any) -> None:
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

    def get(self, key: Input, default=None) -> any:
        """time complexity: O(N)
        average time complexity: O(1) if there isn't many hash value collisions
        """
        index = self._get_index(key)
        for k, v in self.map[index]:
            if k == key:
                return v
        return default

    def remove(self, key: Input) -> None:
        """time complexity: O(N)
        average time complexity: O(1) if there isn't many hash value collisions
        """
        index = self._get_index(key)
        for i, (k, _) in enumerate(self.map[index]):
            if k == key:
                del self.map[index][i]
                return
        raise KeyError(f"{key} not found")

    def contains(self, key: Input) -> bool:
        """time complexity: O(1)"""
        index = self._get_index(key)
        for k, _ in self.map[index]:
            if k == key:
                return True
        return False

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
