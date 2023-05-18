from pytest import raises
from src.structure.set import Set


#
class TestSet:
    def testInitWithRightInput(self):
        s = Set([1, 2, 3, "d", 1.2, (1, 2)])
        assert 1 in s
        assert "d" in s
        assert 1.2 in s
        assert (1, 2) in s
        assert 4 not in s

    def testINitWithWrongInput(self):
        with raises(TypeError):
            Set([[1, 2]])

    def testContains(self):
        s = Set([1, 2, 3, "d", 1.2, (1, 2)])
        assert s.contains(1)
        assert s.contains("d")
        assert s.contains(1.2)
        assert s.contains((1, 2))
        assert not s.contains((1, 3))

    def testAdd(self):
        s = Set([1, 2, 3, "d", 1.2, (1, 2)])
        assert not s.contains(4)
        s.add(4)
        assert s.contains(4)
        s.add(2)

    def testRemove(self):
        s = Set([1, 2, 3, "d", 1.2, (1, 2)])
        assert s.contains((1, 2))
        s.remove((1, 2))
        assert not s.contains((1, 2))
        s.remove((1, 3))

    def testUnion(self):
        s = Set([1, 2, 3])
        t = Set([3, 4, 5])
        res = s.union(t)
        assert list(res.items.keys()) == [1, 2, 3, 4, 5]

    def testIntersection(self):
        s = Set([1, 2, 3])
        t = Set([3, 4])
        res = s.intersection(t)
        assert list(res.items.keys()) == [3]

    def testDiff(self):
        s = Set([1, 2, 3])
        t = Set([3, 4])
        res = s.diff(t)
        assert list(res.items.keys()) == [1, 2]
