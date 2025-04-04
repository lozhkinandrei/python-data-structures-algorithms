class Queue:
    """
    A list-based queue implementation.
    
    This class implements a queue data structure with standard operations like enqueue, dequeue,
    and size, following the First-In-First-Out (FIFO) principle. The implementation uses 
    a Python list for internal storage.
    """
    
    def __init__(self):
        """
        Initialize an empty queue.
        
        Creates a new queue with no elements.
        
        Time Complexity: O(1)
        """
        self.items = []

    def enqueue(self, item):
        """
        Add an item to the queue.
        
        Parameters:
            item: The item to be added to the queue.
            
        Returns:
            None
            
        Time Complexity: O(n), where n is the number of elements in the queue,
        due to the list insertion operation at the beginning.
        """
        self.items.insert(0, item)

    def dequeue(self):
        """
        Remove and return the front item from the queue.
        
        Returns:
            The item at the front of the queue (the oldest item).
            
        Raises:
            IndexError: If the queue is empty (implicitly raised by list.pop()).
            
        Time Complexity: O(1)
        """
        return self.items.pop()

    def size(self):
        """
        Get the number of items in the queue.
        
        Returns:
            int: The number of items in the queue.
            
        Time Complexity: O(1)
        """
        return len(self.items)

    def is_empty(self):
        """
        Check if the queue is empty.
        
        Returns:
            bool: True if the queue is empty, False otherwise.
            
        Time Complexity: O(1)
        """
        return self.items == []

    def __str__(self):
        """
        Get a string representation of the queue.
        
        Returns:
            str: A string representation of the queue as a list.
            
        Time Complexity: O(n), where n is the number of elements in the queue.
        """
        return str(self.items)

    def __repr__(self):
        """
        Get a detailed string representation of the queue.
        
        Returns:
            str: A detailed string representation of the queue, showing tail and head.
            
        Time Complexity: O(n), where n is the number of elements in the queue.
        """
        return f"Queue: tail -> {str(self.items)} <- head"