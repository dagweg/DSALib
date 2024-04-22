# Data Structures Library | Python & C++

This Python & Cpp library provides a collection of data structures for various computational needs. From graphs to heaps, trees to queues, this library offers a comprehensive set of tools for managing and manipulating data efficiently.
<br>
<br>

# Features

- **MaxHeap**: Create and manipulate max-heap data structures.

- **Graph**: Implement and traverse graphs with ease.

- **BinarySearchTree**: Perform operations on binary search trees.

- **Queue**: Utilize different queue implementations.

- **LinkedList**: Work with linked list data structures.
  ...and more: Additional data structures will be continually added.
  <br>
  <br>

# Installation

You can install Data Structures Library using pip:

pip install DataStructuresLibrary
<br>
<br>

# Usage

```python
from python.heaps.max_heap import MaxHeap

# Create a max-heap

heap = MaxHeap([4, 10, 3, 5, 1, 10, 4])

# Insert elements

heap.insert(8)

# Delete elements

heap.delete()

# Sort elements

sorted_array = heap.heap_sort()

# Check if array is max-heap

is_heap = heap.is_max_heap([4, 10, 3, 5, 1, 10, 4])

# Get heap size

size = heap.get_size()

# Get deleted elements

deleted_elements = heap.deleted()
```

# Goal

To create a huge library of data structures & algorithms that are easily accessible & blazing fast.
The code will be constantly improved (both efficiency & readability wise) & its currently being actively maintained.

# Contributing

Contributions are welcome! Feel free to open issues or pull requests to suggest improvements or add new data structures.

# License

This library is licensed under the MIT License.
