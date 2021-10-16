import unittest

from data_structures.linear.queue import Queue


class TestQueueMethods(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_enqueue(self):
        self.queue.items = [2, 1]
        self.queue.enqueue(3)
        self.assertEqual(self.queue.items, [3, 2, 1])

    def test_dequeue(self):
        self.queue.items = [3, 2, 1]
        self.assertEqual(self.queue.dequeue(), 1)

    def test_size(self):
        self.queue.items = [1, 2]
        self.assertEqual(self.queue.size(), 2)

    def test_is_empty_true(self):
        self.assertEqual(self.queue.is_empty(), True)
        self.queue.enqueue(1)
        self.assertEqual(self.queue.is_empty(), False)

    def test_is_empty_false(self):
        self.queue.items = [1, 2, 3]
        self.assertEqual(self.queue.is_empty(), False)

    def test__str__(self):
        self.queue.items = [1, 2, 3, 4]
        self.assertEqual(str(self.queue), "[1, 2, 3, 4]")

    def test__repr__(self):
        self.queue.items = [1, 2, 3, 4]
        self.assertEqual(repr(self.queue), "Queue: tail -> [1, 2, 3, 4] <- head")
