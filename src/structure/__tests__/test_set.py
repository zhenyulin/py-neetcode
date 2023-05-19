from pytest import raises
from src.structure.set import Set


#
class TestSet:
    def testInitWithRightInputContains(self):
        s = Set([1, 2, 3, "d", 1.2, (1, 2)])
        assert 1 in s
        assert "d" in s
        assert 1.2 in s
        assert (1, 2) in s
        assert 4 not in s

    def testINitWithWrongInput(self):
        with raises(TypeError):
            Set([[1, 2]])

    def testAdd(self):
        s = Set([1, 2, 3, "d", 1.2, (1, 2)])
        assert 4 not in s
        s.add(4)
        assert 4 in s
        s.add(2)

    def testRemove(self):
        s = Set([1, 2, 3, "d", 1.2, (1, 2)])
        assert (1, 2) in s
        s.remove((1, 2))
        assert (1, 2) not in s
        s.remove((1, 3))

    def testUnion(self):
        s = Set([1, 2, 3])
        t = Set([3, 4, 5])
        res = s.union(t)
        assert list(res) == [1, 2, 3, 4, 5]
        union = s | t
        assert list(union) == [1, 2, 3, 4, 5]

    def testIntersection(self):
        s = Set([1, 2, 3])
        t = Set([3, 4])
        res = s.intersection(t)
        assert list(res) == [3]
        intersection = s & t
        assert list(intersection) == [3]

    def testDiff(self):
        s = Set([1, 2, 3])
        t = Set([3, 4])
        res = s.diff(t)
        assert list(res) == [1, 2]
        diff = s - t
        assert list(diff) == [1, 2]
