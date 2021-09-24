import unittest
from data_structures.linear.deque import Deque


class TestDequeMethods(unittest.TestCase):
    def setUp(self):
        self.deque = Deque()

    def test_add_front(self):
        self.deque.add_front(1)
        self.deque.add_front(2)
        self.assertEqual(self.deque.items, [1, 2])

    def test_add_rear(self):
        self.deque.add_rear(1)
        self.deque.add_rear(2)
        self.assertEqual(self.deque.items, [2, 1])

    def test_pop_front(self):
        self.deque.add_front(1)
        self.deque.add_front(2)
        self.assertEqual(self.deque.pop_front(), 2)

    def test_pop_rear(self):
        self.deque.add_rear(1)
        self.deque.add_rear(2)
        self.assertEqual(self.deque.pop_rear(), 2)

    def test_size(self):
        self.deque.add_rear(1)
        self.deque.add_rear(2)
        self.assertEqual(self.deque.size(), 2)

    def test_is_empty(self):
        self.assertEqual(self.deque.is_empty(), True)
        self.deque.add_rear(1)
        self.assertEqual(self.deque.is_empty(), False)

    def test__str__(self):
        self.deque.items = [1, 2, 3, 4]
        self.assertEqual(str(self.deque), "[1, 2, 3, 4]")

    def test__repr__(self):
        self.deque.items = [1, 2, 3, 4]
        self.assertEqual(repr(self.deque), "Deque: rear -> [1, 2, 3, 4] <- front")


if __name__ == "__main__":
    unittest.main()
