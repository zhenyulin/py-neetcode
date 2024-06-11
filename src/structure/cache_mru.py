from .cache_lru import LRUCache, Node


class MRUCache(LRUCache):
    def _pop(self) -> Node:
        """Pop the MRU at head.

        time complexity: O(1)
        """
        node = self.head.next
        node.next.prev = self.head
        self.head.next = node.next
        return node
