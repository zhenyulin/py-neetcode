from pytest import raises

from src.structure.hashmap import HashMap


class TestHashMap:
    def testPutGet(self):
        hm = HashMap()
        hm[1] = "a"
        assert hm[1] == "a"
        hm[1] = "b"
        assert hm[1] == "b"
        hm[11] = "c"
        assert hm[1] == "b"
        assert hm[11] == "c"
        hm[(1, 2)] = "foo"
        assert hm[(1, 2)] == "foo"
        hm["bar"] = 2
        assert hm["bar"] == 2

        hm.put("null")
        assert hm.get("null") is None
        assert hm["null"] is None

        with raises(KeyError):
            hm["undefined"]
            hm.get("undefined")

    def testLength(self):
        hm = HashMap()
        assert len(hm) == 0
        hm[1] = "a"
        assert len(hm) == 1
        hm[1] = "b"
        assert len(hm) == 1
        hm[2] = "b"
        assert len(hm) == 2
        hm.remove(2)
        assert len(hm) == 1

    def testRemove(self):
        hm = HashMap()
        hm[1] = "a"
        assert hm.get(1) == "a"
        hm.remove(1)
        with raises(KeyError):
            hm[1]
        hm[2] = "b"
        del hm[2]
        with raises(KeyError):
            hm[2]

    def testContains(self):
        hm = HashMap()
        assert 1 not in hm
        hm[1] = "a"
        assert 1 in hm
        assert hm.contains(1)

    def testKeys(self):
        hm = HashMap()
        hm[1] = "a"
        hm[2] = "b"
        hm[3] = "c"
        assert hm.keys() == [1, 2, 3]

    def testValues(self):
        hm = HashMap()
        hm[1] = "a"
        hm[2] = "b"
        hm[3] = "c"
        assert hm.values() == ["a", "b", "c"]

    def testItems(self):
        hm = HashMap()
        hm[1] = "a"
        hm[2] = "b"
        hm[3] = "c"
        assert hm.items() == [(1, "a"), (2, "b"), (3, "c")]
