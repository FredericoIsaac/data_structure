# Queueu



## Priority Queues with Binary Heaps

A priority queue acts like a queue in that you dequeue an item by removing it from the front. However, in a priority queue the logical order of items inside a queue is determined by their priority. The highest priority items are at the front of the queue and the lowest priority items are at the back. Thus when you enqueue an item on a priority queue, the new item may move all the way to the front.

The binary heap has two common variations: the min heap, in which the smallest key is always at the front, and the max heap, in which the largest key value is always at the front

### Methods

The basic operations we will implement for our binary heap are as follows:

* BinaryHeap() creates a new, empty, binary heap.
* insert(k) adds a new item to the heap.
* findMin() returns the item with the minimum key value, leaving item in the heap.
* delMin() returns the item with the minimum key value, removing the item from the heap.
* isEmpty() returns true if the heap is empty, false otherwise.
* size() returns the number of items in the heap.
* buildHeap(list) builds a new heap from a list of keys.

## Usefull Links

* Priority Queue: 
    * https://runestone.academy/runestone/books/published/pythonds/Trees/PriorityQueueswithBinaryHeaps.html