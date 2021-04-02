## Queue

<img src="assets/queue/queue.svg"><br/>

A queue is an **ordered** collection of items where the addition of new items happens at one end, called the “rear”, and the removal of existing items occurs at the other end, commonly called the “front”.

The most recently added item in the queue must wait at the end of the collection. This ordering principle is sometimes called **FIFO**, first-in first-out.


### Queue Operations

| Operation     | Big O | Description                                       |
| ------------- | ----- | ------------------------------------------------- |
| enqueue(item) | O(n)  | Adds a new item to the rear of the queue          |
| dequeue()     | O(1)  | Returns and removes the front item from the queue |
| size()        | O(1)  | Returns the number of items in the queue          |
| is_empty()    | O(1)  | Returns True if queue is empty                    |

*Note: Big O depends on the implementation.*

[Back](linear.md)
