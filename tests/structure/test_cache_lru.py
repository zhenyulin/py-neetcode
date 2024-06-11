from src.structure.cache_lru import LRUCache


def testLRUCache():
    cache = LRUCache(2)
    assert cache.capacity == 2
    assert cache.head.next == cache.tail
    assert cache.tail.prev == cache.head

    cache.put(2, "b")
    cache.put(1, "a")
    assert cache.get(1) == "a"
    assert cache.head._get_kv_list() == [(1, "a"), (2, "b")]

    cache.put(3, "c")
    assert cache.get(2) is None
    assert cache.head._get_kv_list() == [(3, "c"), (1, "a")]
