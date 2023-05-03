class Node:
    def __init__(self, val: any = None) -> None:
        self.val = val
        self.prev = None
        self.next = None


class Deque:
    def __init__(self) -> None:
        """time complexity: O(1)"""
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0

    def __len__(self):
        """time complexity: O(1)"""
        return self.length

    def is_empty(self):
        """time complexity: O(1)"""
        return self.length == 0

    def left(self):
        """time complexity: O(1)"""
        if self.is_empty():
            raise IndexError("deque is empty")
        return self.head.next.val

    def right(self):
        """time complexity: O(1)"""
        if self.is_empty():
            raise IndexError("deque is empty")
        return self.tail.prev.val

    def append_left(self, val: any) -> None:
        """time complexity: O(1)"""
        node = Node(val)
        node.next, node.prev = self.head.next, self.head
        self.head.next.prev, self.head.next = node, node
        self.length += 1

    def append(self, val: any) -> None:
        """time complexity: O(1)"""
        node = Node(val)
        node.prev, node.next = self.tail.prev, self.tail
        node.prev.next, node.next.prev = node, node
        self.length += 1

    def pop_left(self):
        """time complexity: O(1)"""
        if self.is_empty():
            raise IndexError("not able to pop from empty deque")
        node = self.head.next
        self.head.next = node.next
        node.next.prev = self.head
        self.length -= 1
        return node.val

    def pop(self):
        """time complexity: O(1)"""
        if self.is_empty():
            raise IndexError("not able to pop from empty deque")
        node = self.tail.prev
        self.tail.prev = node.prev
        node.prev.next = self.tail
        self.length -= 1
        return node.val

    def remove(self, val: any) -> bool:
        """time complexity: O(N)"""
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
