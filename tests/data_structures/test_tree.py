import unittest
from typing import Optional

from data_structures.non_linear.tree import Node


class TestTreeMethods(unittest.TestCase):
    def setUp(self):
        self.tree = Node(1)

    def test_insert_left(self):
        self.tree.insert_left(2)
        self.assertIsNotNone(self.tree.left)
        if self.tree.left:  # Type guard for mypy
            self.assertEqual(self.tree.left.key, 2)
            
        self.tree.insert_left(3)
        self.assertIsNotNone(self.tree.left)
        if self.tree.left:  # Type guard for mypy
            self.assertEqual(self.tree.left.key, 3)
            self.assertIsNotNone(self.tree.left.left)
            if self.tree.left.left:  # Type guard for mypy
                self.assertEqual(self.tree.left.left.key, 2)

    def test_insert_right(self):
        self.tree.insert_right(2)
        self.assertIsNotNone(self.tree.right)
        if self.tree.right:  # Type guard for mypy
            self.assertEqual(self.tree.right.key, 2)
            
        self.tree.insert_right(3)
        self.assertIsNotNone(self.tree.right)
        if self.tree.right:  # Type guard for mypy
            self.assertEqual(self.tree.right.key, 3)
            self.assertIsNotNone(self.tree.right.right)
            if self.tree.right.right:  # Type guard for mypy
                self.assertEqual(self.tree.right.right.key, 2)

    def test_preorder(self):
        self.tree.insert_left(2)
        self.tree.insert_right(3)
        self.assertIsNotNone(self.tree.left)
        if self.tree.left:  # Type guard for mypy
            self.tree.left.insert_left(4)
            self.tree.left.insert_right(5)
        self.assertEqual(self.tree.preorder(), [1, 2, 4, 5, 3])

    def test_postorder(self):
        self.tree.insert_left(2)
        self.tree.insert_right(3)
        self.assertIsNotNone(self.tree.left)
        if self.tree.left:  # Type guard for mypy
            self.tree.left.insert_left(4)
            self.tree.left.insert_right(5)
        self.assertEqual(self.tree.postorder(), [4, 5, 2, 3, 1])

    def test_inorder(self):
        self.tree.insert_left(2)
        self.tree.insert_right(3)
        self.assertIsNotNone(self.tree.left)
        if self.tree.left:  # Type guard for mypy
            self.tree.left.insert_left(4)
            self.tree.left.insert_right(5)
        self.assertEqual(self.tree.inorder(), [4, 2, 5, 1, 3])

    def test_breadth_first_traversal(self):
        self.tree.insert_left(2)
        self.tree.insert_right(3)
        self.assertIsNotNone(self.tree.left)
        if self.tree.left:  # Type guard for mypy
            self.tree.left.insert_left(4)
            self.tree.left.insert_right(5)
        self.assertEqual(self.tree.breadth_first_traversal(), [1, 2, 3, 4, 5])