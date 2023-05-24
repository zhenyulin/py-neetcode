from unittest.mock import patch

from src.structure.message_queue_scheduled import ScheduledMessage, MessageQueue


class TestMessageQueue:
    def testEnqueue(self):
        mq = MessageQueue(window_size=100, rate_limit=2)
        assert mq.enqueue(ScheduledMessage("abc", 1000)) is True
        assert mq.enqueue(ScheduledMessage("abc" * 10, 1050)) is False
        assert mq.enqueue(ScheduledMessage("abc", 980)) is False
        assert mq.enqueue(ScheduledMessage("abc", 1010)) is False
        assert mq.enqueue(ScheduledMessage("abc", 1050)) is True
        assert mq.enqueue(ScheduledMessage("abc", 1800)) is True
        assert mq.enqueue(ScheduledMessage("abc", 1080)) is False

    def testEnqueueFullWindowSize(self):
        mq = MessageQueue(window_size=100, rate_limit=2)
        mq.enqueue(ScheduledMessage("abc", 1000))
        mq.enqueue(ScheduledMessage("abc", 1050))
        mq.enqueue(ScheduledMessage("abc", 1100))
        mq.enqueue(ScheduledMessage("abc", 1150))
        assert len(mq.queue) == 4

    @patch("src.structure.message_queue_scheduled.time", return_value=1020)
    @patch("src.structure.message_queue_scheduled.sleep")
    def testDequeue(self, time_mock, sleep_mock):
        mq = MessageQueue(window_size=100, rate_limit=2)
        mq.enqueue(ScheduledMessage("abc", 1000))
        mq.enqueue(ScheduledMessage("abc", 1050))
        mq.enqueue(ScheduledMessage("abc", 1100))
        mq.enqueue(ScheduledMessage("abc", 1150))
        assert len(mq.queue) == 4
        mq.dequeue()
        assert len(mq.queue) == 2
        assert mq.queue == [(1150, 1120, "abc"), (1100, 1070, "abc")]
