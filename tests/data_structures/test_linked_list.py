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
        self.list.add(1)
        self.list.add(2)
        self.list.add(3)
        self.list.add(4)
        # should return value from the tail
        self.assertEqual(self.list.pop(), 1)
        # should return value from the head
        self.assertEqual(self.list.pop(0), 4)
        # after pop operations above [3, 2] left
        # pos 1 would mean value 2
        self.assertEqual(self.list.pop(1), 2)

    def test_pop_empty_list(self):
        self.assertRaises(IndexError, self.list.pop)

    def test_pop_index_out_of_range(self):
        self.list.add(1)
        self.list.add(2)
        self.assertRaises(IndexError, self.list.pop, 5)

    def test_pop_index_error(self):
        self.list.add(1)
        self.list.add(2)
        self.assertRaises(IndexError, self.list.pop, 3)

    def test_size(self):
        self.list.add(1)
        self.assertEqual(self.list.size(), 1)

    def test_is_empty_true(self):
        self.assertEqual(self.list.is_empty(), True)

    def test_is_empty_false(self):
        self.list.add(1)
        self.assertEqual(self.list.is_empty(), False)

    def test__str__(self):
        self.list.add(1)
        self.list.add(2)
        self.list.add(3)
        self.assertEqual(str(self.list), "[3, 2, 1]")

    def test__repr__(self):
        self.list.add(1)
        self.list.add(2)
        self.list.add(3)
        self.assertEqual(repr(self.list), "Linked List: head -> [3, 2, 1] <- tail")
