class Node:
    def __init__(self, val: any = None) -> None:
        self.val = val
        self.prev = None
        self.next = None


class Deque:
    def __init__(self) -> None:
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0

    def __len__(self):
        return self.length

    def is_empty(self):
        return self.length == 0

    def left(self):
        if self.is_empty():
            raise IndexError("deque is empty")
        return self.head.next.val

    def right(self):
        if self.is_empty():
            raise IndexError("deque is empty")
        return self.tail.prev.val

    def append_left(self, val: any) -> None:
        node = Node(val)
        node.next, node.prev = self.head.next, self.head
        self.head.next.prev, self.head.next = node, node
        self.length += 1

    def append(self, val: any) -> None:
        node = Node(val)
        node.prev, node.next = self.tail.prev, self.tail
        node.prev.next, node.next.prev = node, node
        self.length += 1

    def pop_left(self):
        if self.is_empty():
            raise IndexError("not able to pop from empty deque")
        node = self.head.next
        self.head.next = node.next
        node.next.prev = self.head
        self.length -= 1
        return node.val

    def pop(self):
        if self.is_empty():
            raise IndexError("not able to pop from empty deque")
        node = self.tail.prev
        self.tail.prev = node.prev
        node.prev.next = self.tail
        self.length -= 1
        return node.val
