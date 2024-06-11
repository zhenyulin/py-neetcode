from pytest import raises

from src.structure.deque import Deque


class TestDeque:
    def testInitIter(self):
        q = Deque([1, 2, 3])
        assert list(q) == [1, 2, 3]

    def testGetter(self):
        q = Deque([1, 2, 3])
        assert q[0] == 1
        assert q[1] == 2
        assert q[2] == 3
        assert q[-1] == 3
        assert q[-2] == 2
        assert q[-3] == 1

        with raises(IndexError):
            q[-4]

        with raises(IndexError):
            q[3]

    def testSetter(self):
        q = Deque([1, 2, 3])
        q[0] = 4
        assert q[0] == 4
        q[-1] = 0
        assert q[-1] == 0

        with raises(IndexError):
            q[4] = 0

        with raises(IndexError):
            q[-4] = 0

    def testIsEmpty(self):
        q = Deque()
        assert q.is_empty()
        assert not q
        q = Deque([1])
        assert not q.is_empty()
        assert q

    def testAppendLeft(self):
        q = Deque()
        q.append_left(3)
        q.append_left(2)
        q.append_left(1)
        assert list(q) == [1, 2, 3]
        assert q[0] == 1

    def testPopLeft(self):
        q = Deque([1, 2, 3])
        assert q.pop_left() == 1
        assert q.pop_left() == 2
        assert q.pop_left() == 3

    def testAppend(self):
        q = Deque()
        q.append(1)
        q.append(2)
        q.append(3)
        assert list(q) == [1, 2, 3]
        assert q[-1] == 3

    def testPop(self):
        q = Deque([1, 2, 3])
        assert q.pop() == 3
        assert q.pop() == 2
        assert q.pop() == 1

    def testRemove(self):
        q = Deque([1, 2, 3])
        q.remove(2)
        assert list(q) == [1, 3]
        q.remove(4)
        assert list(q) == [1, 3]
