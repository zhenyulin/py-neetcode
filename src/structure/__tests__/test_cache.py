from src.structure.cache import LRUCache


def testLRUCache():
    cache = LRUCache(2)
    assert cache.capacity == 2
    assert cache.head.next == cache.tail
    assert cache.tail.prev == cache.head
    cache.put(2, "b")
    assert cache.head.next.key == 2
    assert cache.tail.prev.key == 2
    cache.put(1, "a")
    assert cache.head.next.key == 1
    assert cache.tail.prev.key == 2
    assert cache.get(1) == "a"
    assert cache.head.next.key == 1
    cache.put(3, "c")
    assert cache.head.next.key == 3
    assert cache.get(2) is None
