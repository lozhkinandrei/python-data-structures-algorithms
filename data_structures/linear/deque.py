from typing import Any, List


class Deque:
    """
    A list-based double-ended queue implementation.
    
    This class implements a deque (double-ended queue) data structure with operations
    for adding and removing elements from both ends. The implementation uses a Python
    list for internal storage, allowing efficient operations at both ends.
    """
    
    def __init__(self) -> None:
        """
        Initialize an empty deque.
        
        Creates a new deque with no elements.
        
        Time Complexity: O(1)
        """
        self.items: List[Any] = []

    def add_front(self, item: Any) -> None:
        """
        Add an item to the front of the deque.
        
        Parameters:
            item: The item to be added to the front.
            
        Returns:
            None
            
        Time Complexity: O(1) amortized
        """
        self.items.append(item)

    def add_rear(self, item: Any) -> None:
        """
        Add an item to the rear of the deque.
        
        Parameters:
            item: The item to be added to the rear.
            
        Returns:
            None
            
        Time Complexity: O(n), where n is the number of elements in the deque,
        due to the list insertion operation at the beginning.
        """
        self.items.insert(0, item)

    def pop_front(self) -> Any:
        """
        Remove and return the item from the front of the deque.
        
        Returns:
            The item at the front of the deque.
            
        Raises:
            IndexError: If the deque is empty (implicitly raised by list.pop()).
            
        Time Complexity: O(1)
        """
        return self.items.pop()

    def pop_rear(self) -> Any:
        """
        Remove and return the item from the rear of the deque.
        
        Returns:
            The item at the rear of the deque.
            
        Raises:
            IndexError: If the deque is empty (implicitly raised by list.pop()).
            
        Time Complexity: O(n), where n is the number of elements in the deque,
        because removing an element from the beginning of a list requires shifting all other elements.
        """
        return self.items.pop(0)

    def size(self) -> int:
        """
        Get the number of items in the deque.
        
        Returns:
            int: The number of items in the deque.
            
        Time Complexity: O(1)
        """
        return len(self.items)

    def is_empty(self) -> bool:
        """
        Check if the deque is empty.
        
        Returns:
            bool: True if the deque is empty, False otherwise.
            
        Time Complexity: O(1)
        """
        return self.items == []

    def __str__(self) -> str:
        """
        Get a string representation of the deque.
        
        Returns:
            str: A string representation of the deque as a list.
            
        Time Complexity: O(n), where n is the number of elements in the deque.
        """
        return str(self.items)

    def __repr__(self) -> str:
        """
        Get a detailed string representation of the deque.
        
        Returns:
            str: A detailed string representation of the deque, showing rear and front.
            
        Time Complexity: O(n), where n is the number of elements in the deque.
        """
        return f"Deque: rear -> {str(self.items)} <- front"