from src.structure.hashmap import HashMap


class TestHashMap:
    def testPutGet(self):
        hm = HashMap()
        hm.put(1, "a")
        assert hm.get(1) == "a"
        hm.put(1, "b")
        assert hm.get(1) == "b"
        hm.put(11, "c")
        assert hm.get(1) == "b"
        assert hm.get(11) == "c"
        hm.put((1, 2), "foo")
        assert hm.get((1, 2)) == "foo"
        hm.put("bar", 2)
        assert hm.get("bar") == 2

    def testRemove(self):
        hm = HashMap()
        hm.put(1, "a")
        assert hm.get(1) == "a"
        hm.remove(1)
        assert hm.get(1) is None

    def testContains(self):
        hm = HashMap()
        assert not hm.contains(1)
        hm.put(1, "a")
        assert hm.contains(1)

    def testKeys(self):
        hm = HashMap()
        hm.put(1, "a")
        hm.put(2, "b")
        hm.put(3, "c")
        assert hm.keys() == [1, 2, 3]

    def testValues(self):
        hm = HashMap()
        hm.put(1, "a")
        hm.put(2, "b")
        hm.put(3, "c")
        assert hm.values() == ["a", "b", "c"]

    def testItems(self):
        hm = HashMap()
        hm.put(1, "a")
        hm.put(2, "b")
        hm.put(3, "c")
        assert hm.items() == [(1, "a"), (2, "b"), (3, "c")]
