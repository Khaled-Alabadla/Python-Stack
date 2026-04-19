# Linked Lists Documentation

This repository contains Python implementations of Singly and Doubly Linked Lists, developed to master data structure fundamentals and prepare for technical interviews.

## 1. Singly Linked List (`singly_linked_list.py`)

A basic linear data structure where each node points only to the next node.

### Key Methods:
- `add_to_front(val)`: Adds a node at the beginning of the list.
- `add_to_back(val)`: Adds a node at the end of the list.
- `print_values()`: Traverses and prints all values in order.
- `remove_from_front()` / `remove_from_back()`: Deletes the head or tail node.
- `remove_val(val)`: Removes the first node containing the specified value.
- `insert_at(val, n)`: Inserts a node at the nth position.

---

## 2. Doubly Linked List (`doubly_linked_list.py`)

An advanced data structure where each node contains pointers to both the **next** and **previous** nodes, allowing for bidirectional traversal.

### Key Methods:
- `add_to_front(val)` / `add_to_back(val)`: efficient additions to either end.
- `insert_at(val, index)`: Inserts a node at any given index.
- `remove_val(val)`: Removes a node by value, updating both forward and backward pointers.
- `print_values()`: Forward traversal (Head -> Tail).
- `print_values_backward()`: Backward traversal (Tail -> Head).

## Usage
Run the following command to see the Singly Linked List file:
```bash
python doubly_linked_list.py
```
Run the following command to see the Doubly Linked List file:
```bash
python doubly_linked_list.py
```
