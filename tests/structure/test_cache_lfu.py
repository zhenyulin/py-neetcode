from src.structure.cache_lfu import LFUCache


def testLFUCache():
    cache = LFUCache(3)
    cache.put("a", 1)
    cache.put("b", 2)
    cache.put("c", 3)
    cache.get("b")
    cache.get("b")
    cache.get("c")
    cache.put("d", 4)
    assert cache.get("a") is None
    cache.get("d")
    cache.get("d")
    cache.put("e", 5)
    cache.get("e")
    assert cache.get("c") is None
    cache.put("d", 0)
    cache.put("f", 6)
    assert cache.get("d") is None
