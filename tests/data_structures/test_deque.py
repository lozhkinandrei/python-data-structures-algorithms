import unittest

from data_structures.linear.deque import Deque


class TestDequeMethods(unittest.TestCase):
    def setUp(self):
        self.deque = Deque()

    def test_add_front(self):
        self.deque.items = [1, 2]
        self.deque.add_front(3)
        self.assertEqual(self.deque.items, [1, 2, 3])

    def test_add_rear(self):
        self.deque.items = [1, 2]
        self.deque.add_rear(3)
        self.assertEqual(self.deque.items, [3, 1, 2])

    def test_pop_front(self):
        self.deque.items = [1, 2, 3]
        self.assertEqual(self.deque.pop_front(), 3)
        self.assertEqual(self.deque.items, [1, 2])

    def test_pop_rear(self):
        self.deque.items = [1, 2, 3]
        self.assertEqual(self.deque.pop_rear(), 1)
        self.assertEqual(self.deque.items, [2, 3])

    def test_size(self):
        self.deque.items = [1, 2]
        self.assertEqual(self.deque.size(), 2)

    def test_is_empty_true(self):
        self.assertEqual(self.deque.is_empty(), True)

    def test_is_empty_false(self):
        self.deque.items = [1, 2, 3]
        self.assertEqual(self.deque.is_empty(), False)

    def test__str__(self):
        self.deque.items = [1, 2, 3, 4]
        self.assertEqual(str(self.deque), "[1, 2, 3, 4]")

    def test__repr__(self):
        self.deque.items = [1, 2, 3, 4]
        self.assertEqual(repr(self.deque), "Deque: rear -> [1, 2, 3, 4] <- front")
