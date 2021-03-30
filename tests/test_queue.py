import unittest
from data_structures.linear.queue import queue


class TestQueueMethods(unittest.TestCase):
    def setUp(self):
        self.queue = queue.Queue()

    def test_enqueue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.items, [2, 1])

    def test_dequeue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.dequeue(), 1)

    def test_size(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.size(), 2)

    def test_is_empty(self):
        self.assertEqual(self.queue.is_empty(), True)
        self.queue.enqueue(1)
        self.assertEqual(self.queue.is_empty(), False)


if __name__ == '__main__':
    unittest.main()
