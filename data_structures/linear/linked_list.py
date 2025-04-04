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
        
        Raises:
            ValueError: If the value is not found in the list.
        
        Time Complexity: O(n), where n is the number of elements in the list.
        """
        if self.head is None:
            raise ValueError("Value not found in list")

        # Handle head node case
        if self.head.value == value:
            self.head = self.head.next
            self._size -= 1
            return

        prev = self.head
        current = prev.next

        while current is not None:
            if current.value == value:
                prev.next = current.next
                self._size -= 1
                return
            prev = current
            current = current.next

        raise ValueError("Value not found in list")

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
                - If 0: remove from head
                - If None: remove last element
                - Other integers: remove at specified position
        
        Returns:
            The value of the removed element.
        
        Raises:
            IndexError: If list is empty or position is out of bounds
        
        Time Complexity:
            - O(1) for head removal
            - O(n) for other cases
        """
        if self.head is None:
            raise IndexError("pop from empty list")

        # Handle head removal
        if pos == 0:
            value = self.head.value
            self.head = self.head.next
            self._size -= 1
            return value

        # Handle specified position
        if pos is not None:
            if pos < 0 or pos >= self._size:
                raise IndexError("pop index out of range")
            
            prev: Optional[Node] = None
            current: Optional[Node] = self.head
            index = 0

            while current and index < pos:
                prev = current
                current = current.next
                index += 1

            if current is None:
                raise IndexError("pop index out of range")

            if prev:
                prev.next = current.next
            else:
                self.head = current.next
            
            self._size -= 1
            return current.value

        # Handle last element removal
        assert self.head is not None  # Ensured by earlier check
        last_prev: Optional[Node] = None
        last_current: Node = self.head
        while last_current.next is not None:
            last_prev = last_current
            last_current = last_current.next

        value = last_current.value
        if last_prev:
            last_prev.next = None
        else:
            self.head = None
        
        self._size -= 1
        return value

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