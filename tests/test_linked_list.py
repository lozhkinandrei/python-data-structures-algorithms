import unittest
from data_structures.linear.linked_list import LinkedList


class TestLinkedListMethods(unittest.TestCase):
    def setUp(self):
        self.list = LinkedList()

    def test_add(self):
        self.list.add(1)
        self.assertEqual(self.list.index(1), 0)
        self.list.add(2)
        self.assertEqual(self.list.index(2), 0)
        self.list.add(3)
        self.assertEqual(self.list.index(3), 0)

    def test_append(self):
        self.list.append(1)
        self.assertEqual(self.list.index(1), 0)
        self.list.append(2)
        self.assertEqual(self.list.index(2), 1)
        self.list.append(3)
        self.assertEqual(self.list.index(3), 2)

    def test_search(self):
        self.list.add(1)
        self.list.add(2)
        self.assertEqual(self.list.search(2), True)
        self.assertEqual(self.list.search(3), False)

    def test_remove(self):
        self.assertRaises(ValueError, self.list.remove, 1)
        self.list.add(1)
        self.list.add(2)
        self.list.add(3)
        self.assertEqual(self.list.remove(2), None)
        self.assertEqual(self.list.search(2), False)

    def test_index(self):
        self.assertRaises(ValueError, self.list.index, 1)
        self.list.add(1)
        self.list.add(2)
        self.list.add(3)
        self.assertEqual(self.list.index(3), 0)

    def test_pop(self):
        self.assertRaises(IndexError, self.list.pop)
        self.assertRaises(IndexError, self.list.pop, 1)
        self.list.add(1)
        self.list.add(2)
        self.list.add(3)
        self.list.add(4)
        self.assertEqual(self.list.pop(), 1)
        self.assertEqual(self.list.pop(1), 3)
        self.assertEqual(self.list.size(), 2)

    def test_size(self):
        self.assertEqual(self.list.size(), 0)
        self.list.add(1)
        self.assertEqual(self.list.size(), 1)

    def test_is_empty(self):
        self.assertEqual(self.list.is_empty(), True)
        self.list.add(1)
        self.assertEqual(self.list.is_empty(), False)

    def test__str__(self):
        self.assertEqual(self.list.__str__(), '(None)')
        self.list.add(1)
        self.list.add(2)
        self.list.add(3)
        self.assertEqual(self.list.__str__(), '(3) => (2) => (1) => (None)')


if __name__ == '__main__':
    unittest.main()
