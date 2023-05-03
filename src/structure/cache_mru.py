from .cache_lru import Node, LRUCache


class MRUCache(LRUCache):
    def _pop(self) -> Node:
        """
        pop the MRU at head

        time complexity: O(1)
        """
        node = self.head.next
        node.next.prev = self.head
        self.head.next = node.next
        return node
