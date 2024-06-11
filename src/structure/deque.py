#
# https://wiki.python.org/moin/TimeComplexity
#
# using a index_map {} for O(1) getter and setter
# would result in appendLeft and PopLeft being O(N)
#
from typing import Optional


class Node:
    def __init__(self, val: any = None) -> None:
        self.val = val
        self.prev = None
        self.next = None


class Deque:
    def __init__(self, elements: Optional[list[any]] = []) -> None:
        """Time complexity: O(N)."""
        self.head = None
        self.tail = None
        self.length = 0

        for e in elements:
            self.append(e)

    def __len__(self):
        """Time complexity: O(1)."""
        return self.length

    def __iter__(self):
        """Time complexity: O(N)."""
        node = self.head
        while node:
            yield node.val
            node = node.next

    def __getitem__(self, index: int) -> any:
        """Time complexity: O(N)."""
        _index = index if index >= 0 else self.length + index

        if not 0 <= _index < self.length:
            raise IndexError("index out of range")
        node = self.head
        for _ in range(_index):
            node = node.next
        return node.val

    def __setitem__(self, index: int, value: any) -> None:
        """Time complexity: O(N)."""
        _index = index if index >= 0 else self.length + index

        if not 0 <= _index < self.length:
            raise IndexError("index out of range")

        node = self.head
        for _ in range(_index):
            node = node.next
        node.val = value

    def __bool__(self) -> bool:
        return not self.is_empty()

    def is_empty(self):
        """Time complexity: O(1)."""
        return self.length == 0

    def append_left(self, val: any) -> None:
        """Time complexity: O(1)."""
        node = Node(val)
        if self.is_empty():
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.length += 1

    def append(self, val: any) -> None:
        """Time complexity: O(1)."""
        node = Node(val)
        if self.is_empty():
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.length += 1

    def pop_left(self):
        """Time complexity: O(1)."""
        if self.is_empty():
            raise IndexError("not able to pop from empty deque")
        val = self.head.val
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.length -= 1
        return val

    def pop(self):
        """Time complexity: O(1)."""
        if self.is_empty():
            raise IndexError("not able to pop from empty deque")
        val = self.tail.val
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1
        return val

    def remove(self, val: any) -> bool:
        """Time complexity: O(N)."""
        node = self.head
        while node:
            if node.val == val:
                if node.prev is None:
                    self.pop_left()
                elif node.next is None:
                    self.pop()
                else:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                self.length -= 1
                return True
            node = node.next
        return False
