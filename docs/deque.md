## Deque

<img src="assets/deque/deque.svg"><br/>

A deque, also known as a double-ended queue, is an ordered collection of items similar to the queue. It has two ends, and new items can be added at either the front or the rear. Likewise, existing items can be removed from either end.

### Deque Operations

| Operation       | Big O | Description                                       |
| --------------- | ----- | ------------------------------------------------- |
| add_front(item) | O(1)  | Adds a new item to the front of the deque         |
| add_rear(item)  | O(n)  | Adds a new item to the rear of the deque          |
| pop_front()     | O(1)  | Removes and returns the front item from the deque |
| pop_rear()      | O(n)  | Removes and returns the rear item from the deque  |
| size()          | O(1)  | Returns the number of items in the deque          |
| is_empty()      | O(1)  | Returns True if deque is empty                    |

*Note: Big O depends on the implementation.*

[Back](linear.md)
