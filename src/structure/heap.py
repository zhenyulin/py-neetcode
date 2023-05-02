class Heap:
    def __init__(self) -> None:
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def __str__(self):
        return str(self.heap)

    def _parent(self, i: int) -> int:
        """
        represent a binary tree in list format
        """
        return (i - 1) // 2

    def _left(self, i: int) -> int:
        return 2 * i + 1

    def _right(self, i: int) -> int:
        return 2 * i + 2

    def _swap(self, i: int, j: int) -> None:
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _move_up(self, i: int) -> None:
        """
        move the smaller up

        time complexity: O(logN)
        """
        parent = self._parent(i)
        while i > 0 and self.heap[i] < self.heap[parent]:
            self._swap(i, parent)
            i = parent

    def _move_down(self, i) -> None:
        """
        move the bigger down

        time complexity: O(logN)
        """
        min_index, left, right = i, self._left(i), self._right(i)

        if left < len(self.heap) and self.heap[min_index] > self.heap[left]:
            min_index = left
        if right < len(self.heap) and self.heap[min_index] > self.heap[right]:
            min_index = right
        if i != min_index:
            self._swap(i, min_index)
            self._move_down(min_index)

    def push(self, val) -> None:
        """
        time complexity: O(logN)
        """
        self.heap.append(val)
        self._move_up(len(self.heap) - 1)

    def pop(self) -> None:
        """
        time complexity: O(logN)
        """
        if not self.heap:
            raise IndexError("not able to pop from empty heap")
        self._swap(0, len(self.heap) - 1)
        val = self.heap.pop()
        self._move_down(0)
        return val

    def peek(self) -> None:
        if not self.heap:
            raise IndexError("heap is empty")
        return self.heap[0]
