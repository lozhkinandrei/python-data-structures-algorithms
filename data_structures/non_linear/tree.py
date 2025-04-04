from typing import Optional, Any, List, TypeVar, Generic
from queue import Queue as PyQueue


class Node:
    """
    A node in a binary tree.
    
    This class represents a node in a binary tree, containing a key value and references
    to left and right child nodes. It also provides methods for tree traversal and node insertion.
    """
    
    def __init__(self, key: Any, left: Optional['Node'] = None, right: Optional['Node'] = None) -> None:
        """
        Initialize a new binary tree node.
        
        Parameters:
            key: The value to be stored in the node.
            left (Node, optional): Reference to the left child node. Defaults to None.
            right (Node, optional): Reference to the right child node. Defaults to None.
        
        Time Complexity: O(1)
        """
        self.key: Any = key
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None

    def insert_left(self, key: Any) -> None:
        """
        Insert a new node as the left child.
        
        If a left child already exists, the new node becomes the left child
        and the existing left child becomes the left child of the new node.
        
        Parameters:
            key: The value to be stored in the new node.
            
        Returns:
            None
            
        Time Complexity: O(1)
        """
        if self.left:
            temp = Node(key)
            temp.left = self.left
            self.left = temp
        else:
            self.left = Node(key)

    def insert_right(self, key: Any) -> None:
        """
        Insert a new node as the right child.
        
        If a right child already exists, the new node becomes the right child
        and the existing right child becomes the right child of the new node.
        
        Parameters:
            key: The value to be stored in the new node.
            
        Returns:
            None
            
        Time Complexity: O(1)
        """
        if self.right:
            temp = Node(key)
            temp.right = self.right
            self.right = temp
        else:
            self.right = Node(key)

    def preorder(self) -> List[Any]:
        """
        Perform a preorder traversal starting from this node.
        
        Preorder traversal visits the current node first, then recursively
        visits the left subtree, and finally recursively visits the right subtree.
        (Root -> Left -> Right)
        
        Returns:
            list: A list containing the keys in preorder traversal order.
            
        Time Complexity: O(n), where n is the number of nodes in the tree.
        """
        result = []

        result.append(self.key)

        if self.left:
            result += self.left.preorder()
        if self.right:
            result += self.right.preorder()

        return result

    def postorder(self) -> List[Any]:
        """
        Perform a postorder traversal starting from this node.
        
        Postorder traversal recursively visits the left subtree first, then
        recursively visits the right subtree, and finally visits the current node.
        (Left -> Right -> Root)
        
        Returns:
            list: A list containing the keys in postorder traversal order.
            
        Time Complexity: O(n), where n is the number of nodes in the tree.
        """
        result = []

        if self.left:
            result += self.left.postorder()
        if self.right:
            result += self.right.postorder()

        result.append(self.key)
        return result

    def inorder(self) -> List[Any]:
        """
        Perform an inorder traversal starting from this node.
        
        Inorder traversal recursively visits the left subtree first, then visits
        the current node, and finally recursively visits the right subtree.
        (Left -> Root -> Right)
        
        Returns:
            list: A list containing the keys in inorder traversal order.
            
        Time Complexity: O(n), where n is the number of nodes in the tree.
        """
        result = []

        if self.left:
            result += self.left.inorder()

        result.append(self.key)

        if self.right:
            result += self.right.inorder()

        return result

    def breadth_first_traversal(self) -> List[Any]:
        """
        Perform a breadth-first (level-order) traversal starting from this node.
        
        Breadth-first traversal visits all nodes at the current depth level before
        moving to nodes at the next depth level. It uses a queue to keep track of
        nodes to be visited.
        
        Returns:
            list: A list containing the keys in breadth-first traversal order.
        
        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(w), where w is the maximum width of the tree.
        """
        result = []

        queue: PyQueue['Node'] = PyQueue()
        queue.put(self)

        while queue.qsize() > 0:
            node = queue.get()
            result.append(node.key)

            if node.left:
                queue.put(node.left)

            if node.right:
                queue.put(node.right)

        return result