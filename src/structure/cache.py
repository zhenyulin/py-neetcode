Input = int | float | str | tuple


class Node:
    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity: int) -> None:
        """
        use a dict as cache, and pointed to a linked list for recency

        time complexity: O(1)
        """
        self.capacity = capacity
        self.cache = {}

        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _to_head(self, node: Node) -> None:
        """time complexity: O(1)"""
        node.prev.next, node.next.prev = node.next, node.prev
        node.prev, node.next = self.head, self.head.next
        self.head.next.prev, self.head.next = node, node

    def _pop(self) -> None:
        """time complexity: O(1)"""
        node = self.tail.prev
        node.prev.next = self.tail
        self.tail.prev = node.prev
        return node

    def get(self, key: Input) -> any:
        """time complexity: O(1)"""
        if key in self.cache:
            node = self.cache[key]
            self._to_head(node)
            return node.val
        else:
            return None

    def put(self, key: Input, value: any) -> None:
        """time complexity: O(1)"""
        if key in self.cache:
            node = self.cache[key]
            self._to_head(node)
            node.val = value
        else:
            if len(self.cache) == self.capacity:
                expired = self._pop()
                del self.cache[expired.key]

            node = Node(key, value, self.head, self.head.next)
            self.cache[key] = node
            self.head.next.prev, self.head.next = node, node
