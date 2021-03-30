import unittest
from data_structures.linear.stack import stack


class TestStackMethods(unittest.TestCase):
    def setUp(self):
        self.stack = stack.Stack()

    def test_push(self):
        self.stack.push(1)
        self.assertEqual(self.stack.items, [1])
        self.stack.push(2)
        self.assertEqual(self.stack.items, [1, 2])

    def test_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.items, [1])

    def test_peek(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.peek(), 2)

    def test_size(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.size(), 2)

    def test_is_empty(self):
        self.assertEqual(self.stack.is_empty(), True)
        self.stack.push(1)
        self.assertEqual(self.stack.is_empty(), False)


if __name__ == '__main__':
    unittest.main()
