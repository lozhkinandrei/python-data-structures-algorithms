from typing import Any, List


class Stack:
    """
    A list-based stack implementation.
    
    This class implements a stack data structure with standard operations like push, pop,
    and peek, following the Last-In-First-Out (LIFO) principle. The implementation uses 
    a Python list for internal storage.
    """
    
    def __init__(self) -> None:
        """
        Initialize an empty stack.
        
        Creates a new stack with no elements.
        
        Time Complexity: O(1)
        """
        self.items: List[Any] = []

    def push(self, item: Any) -> None:
        """
        Push an item onto the stack.
        
        Parameters:
            item: The item to be added to the stack.
            
        Returns:
            None
            
        Time Complexity: O(1) amortized
        """
        self.items.append(item)

    def pop(self) -> Any:
        """
        Remove and return the top item from the stack.
        
        Returns:
            The item at the top of the stack.
            
        Raises:
            IndexError: If the stack is empty (implicitly raised by list.pop()).
            
        Time Complexity: O(1)
        """
        return self.items.pop()

    def peek(self) -> Any:
        """
        Return the top item from the stack without removing it.
        
        Returns:
            The item at the top of the stack.
            
        Raises:
            IndexError: If the stack is empty (implicitly when accessing empty list).
            
        Time Complexity: O(1)
        """
        return self.items[-1]

    def size(self) -> int:
        """
        Get the number of items in the stack.
        
        Returns:
            int: The number of items in the stack.
            
        Time Complexity: O(1)
        """
        return len(self.items)

    def is_empty(self) -> bool:
        """
        Check if the stack is empty.
        
        Returns:
            bool: True if the stack is empty, False otherwise.
            
        Time Complexity: O(1)
        """
        return self.items == []

    def __str__(self) -> str:
        """
        Get a string representation of the stack.
        
        Returns:
            str: A string representation of the stack as a list.
            
        Time Complexity: O(n), where n is the number of elements in the stack.
        """
        return str(self.items)

    def __repr__(self) -> str:
        """
        Get a detailed string representation of the stack.
        
        Returns:
            str: A detailed string representation of the stack, showing bottom and top.
            
        Time Complexity: O(n), where n is the number of elements in the stack.
        """
        return f"Stack: bottom -> {str(self.items)} <- top"