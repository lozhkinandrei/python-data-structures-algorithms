import unittest
from data_structures.linear.stack import Stack


class TestStackMethods(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.stack.push(1)
        self.assertEqual(self.stack.items, [1])
        self.stack.push(2)
        self.assertEqual(self.stack.items, [1, 2])

    def test_pop(self):
        self.stack.items = [1, 2]
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.items, [1])

    def test_peek(self):
        self.stack.items = [1, 2]
        self.assertEqual(self.stack.peek(), 2)

    def test_size(self):
        self.stack.items = [1, 2]
        self.assertEqual(self.stack.size(), 2)

    def test_is_empty_true(self):
        self.assertEqual(self.stack.is_empty(), True)

    def test_is_empty_false(self):
        self.stack.items = [1, 2]
        self.assertEqual(self.stack.is_empty(), False)

    def test_str(self):
        self.stack.items = [1, 2, 3]
        self.assertEqual(str(self.stack), "[1, 2, 3]")


if __name__ == "__main__":
    unittest.main()
