from typing import Optional, Any, List


class Node:
    """
    A node in a singly linked list.
    
    This class represents a node in a singly linked list, containing a value and a reference
    to the next node in the sequence.
    """
    
    def __init__(self, value: Any, next: Optional['Node'] = None) -> None:
        """
        Initialize a new node.
        
        Parameters:
            value: The value to be stored in the node.
            next (Node, optional): Reference to the next node. Defaults to None.
        
        Time Complexity: O(1)
        """
        self.value: Any = value
        self.next: Optional['Node'] = next


class LinkedList:
    """
    A singly linked list implementation.
    
    This class implements a singly linked list data structure with standard operations
    like add, append, search, remove, and various other utility methods. The list
    maintains a reference to the head node and tracks its size.
    """
    
    def __init__(self) -> None:
        """
        Initialize an empty linked list.
        
        Creates a new linked list with no nodes and size zero.
        
        Time Complexity: O(1)
        """
        self.head: Optional[Node] = None
        self._size: int = 0

    def add(self, value: Any) -> None:
        """
        Add a new node at the beginning of the linked list.
        
        Parameters:
            value: The value to be stored in the new node.
            
        Returns:
            None
            
        Time Complexity: O(1)
        """
        self.head = Node(value, self.head)
        self._size += 1

    def append(self, value: Any) -> None:
        """
        Add a new node at the end of the linked list.
        
        Parameters:
            value: The value to be stored in the new node.
            
        Returns:
            None
            
        Time Complexity: O(n), where n is the number of elements in the list.
        """
        node = self.head

        if node:
            while node.next:
                node = node.next
            node.next = Node(value)
        else:
            self.head = Node(value)

        self._size += 1

    def search(self, value: Any) -> bool:
        """
        Search for a value in the linked list.
        
        Parameters:
            value: The value to search for.
            
        Returns:
            bool: True if the value is found in the list, False otherwise.
            
        Time Complexity: O(n), where n is the number of elements in the list.
        """
        node = self.head
        while node:
            if node.value == value:
                return True
            node = node.next
        return False

    def remove(self, value: Any) -> None:
        """
        Remove the first occurrence of a value from the linked list.
        
        Parameters:
            value: The value to be removed.
            
        Returns:
            None
            
        Raises:
            ValueError: If the value is not in the list (indirectly via self.index).
            
        Time Complexity: O(n), where n is the number of elements in the list.
        """
        if self.index(value):
            node = self.head
            prev = node

            while node:
                if node.value == value:
                    prev.next = node.next
                    self._size -= 1
                    break
                prev = node
                node = node.next

    def index(self, value: Any) -> int:
        """
        Find the index of the first occurrence of a value in the linked list.
        
        Parameters:
            value: The value to search for.
            
        Returns:
            int: The zero-based index of the value.
            
        Raises:
            ValueError: If the value is not found in the list.
            
        Time Complexity: O(n), where n is the number of elements in the list.
        """
        node = self.head
        index = 0
        while node:
            if node.value == value:
                return index
            index += 1
            node = node.next
        raise ValueError("{} is not in list".format(value))

    def pop(self, pos: Optional[int] = None) -> Any:
        """
        Remove and return an element from the linked list.
        
        Parameters:
            pos (int, optional): The position of the element to remove.
                If None, removes and returns the last element.
                
        Returns:
            The value of the removed element.
            
        Raises:
            IndexError: If the list is empty or the position is out of range.
            
        Time Complexity:
            - O(1) if pos=0 (first element)
            - O(n) otherwise, where n is the number of elements in the list.
        """
        node = self.head
        index = 0

        if node is None:
            raise IndexError("pop from empty list")

        if pos is not None:
            if pos == 0:
                self._size -= 1
                value = self.head.value
                self.head = self.head.next
                return value

            while node.next:
                prev = node
                node = node.next
                index += 1
                if index == pos:
                    self._size -= 1
                    prev.next = node.next
                    return node.value
            raise IndexError("pop index out of range")

        while node.next:
            prev = node
            node = node.next
        prev.next = None
        self._size -= 1
        return node.value

    def size(self) -> int:
        """
        Get the number of elements in the linked list.
        
        Returns:
            int: The number of elements in the list.
            
        Time Complexity: O(1)
        """
        return self._size

    def is_empty(self) -> bool:
        """
        Check if the linked list is empty.
        
        Returns:
            bool: True if the list is empty, False otherwise.
            
        Time Complexity: O(1)
        """
        return self.head is None

    def __str__(self) -> str:
        """
        Get a string representation of the linked list.
        
        Returns:
            str: A string representation of the list as an array of values.
            
        Time Complexity: O(n), where n is the number of elements in the list.
        """
        items = []
        node = self.head

        while node:
            items.append(node.value)
            node = node.next

        return str(items)

    def __repr__(self) -> str:
        """
        Get a detailed string representation of the linked list.
        
        Returns:
            str: A detailed string representation of the list, showing direction from head to tail.
            
        Time Complexity: O(n), where n is the number of elements in the list.
        """
        items = []
        node = self.head
        while node:
            items.append(node.value)
            node = node.next

        return f"Linked List: head -> {str(items)} <- tail"