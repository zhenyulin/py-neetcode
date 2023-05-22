from typing import Self
from .hashmap import Input


class Node:
    def __init__(
        self,
        key: Input = None,
        val: any = None,
        prev: Self = None,
        next: Self = None,
    ) -> None:
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

    def _get_kv_list(self) -> list[tuple[Input, any]]:
        res, node = [], self
        while node:
            if node.key:
                res.append((node.key, node.val))
            node = node.next
        return res


class LRUCache:
    """
    1) dict & linked list
    use a dict as cache, and pointed to a linked list for recency

    get: O(1), put: O(1)
    """

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache = {}

        # create empty head and tail node so there's no need for null check
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _to_head(self, node: Node) -> None:
        """time complexity: O(1)"""
        node.prev.next, node.next.prev = node.next, node.prev
        node.prev, node.next = self.head, self.head.next
        self.head.next.prev, self.head.next = node, node

    def _pop(self) -> Node:
        """
        pop the LRU at tail

        time complexity: O(1)
        """
        node = self.tail.prev
        node.prev.next = self.tail
        self.tail.prev = node.prev
        return node

    def get(self, key: Input) -> any:
        """
        get the value and update the recency by moving the node to head

        time complexity: O(1)
        """
        if key in self.cache:
            node = self.cache[key]
            self._to_head(node)
            return node.val
        else:
            return None

    def put(self, key: Input, value: any) -> None:
        """
        update to the head side, pop the LRU at tail

        time complexity: O(1)
        """
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
