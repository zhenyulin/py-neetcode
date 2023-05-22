from src.structure.cache_priority import PriorityCache


class TestPriorityQueue:
    def testAdd(self):
        cache = PriorityCache(capacity=3)
        cache.add("foo", 0, 2)
        cache.add("bar", 0, 1)
        cache.add("hey", 0, 3)
        assert list(cache.priority) == [(3, "hey"), (2, "foo"), (1, "bar")]
        assert cache.cache == {"foo": 0, "bar": 0, "hey": 0}
        cache.add("yo", 0, 4)
        assert list(cache.priority) == [(4, "yo"), (3, "hey"), (2, "foo")]
        assert cache.cache == {"foo": 0, "yo": 0, "hey": 0}

    def testPop(self):
        cache = PriorityCache()
        cache.add("foo", 2, 2)
        cache.add("bar", 1, 1)
        cache.add("hey", 3, 3)
        assert cache.pop() == 1

    def testGet(self):
        cache = PriorityCache()
        cache.add("foo", 2, 2)
        cache.add("bar", 1, 1)
        cache.add("hey", 3, 3)
        assert cache.get("foo") == 2
        assert cache.get("bar") == 1

    def testUpdateValue(self):
        cache = PriorityCache()
        cache.add("foo", 2, 2)
        cache.add("bar", 1, 1)
        cache.add("hey", 3, 3)
        cache.update_value("hey", 4)
        assert cache.get("hey") == 4

    def testUpdatePriority(self):
        cache = PriorityCache()
        cache.add("foo", 2, 2)
        cache.add("bar", 1, 1)
        cache.add("hey", 3, 3)
        cache.update_priority("bar", 4)
        assert list(cache.priority) == [(4, "bar"), (3, "hey"), (2, "foo")]
        assert cache.cache == {"foo": 2, "bar": 1, "hey": 3}
