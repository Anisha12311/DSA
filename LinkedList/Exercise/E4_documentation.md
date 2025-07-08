# Circular Linked List Implementation

This document provides documentation for the circular linked list implementation in `E4.py`.

## Class Overview

### Node Class

The `Node` class represents a single node in the circular linked list.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

**Attributes:**

- `data`: Holds the value stored in the node
- `next`: Points to the next node in the list

### Circle Class

The `Circle` class implements a circular linked list where the last node points back to the first node.

```python
class circle:
    def __init__(self):
        self.head = None
        self.tail = None
```

**Attributes:**

- `head`: Points to the first node in the list
- `tail`: Points to the last node in the list

## Methods

### Insert

Adds a new node at the end of the list.

```python
def insert(self, data):
    # Implementation details...
```

**Parameters:**

- `data`: The value to store in the new node

**Behavior:**

- If the list is empty, the new node becomes both head and tail
- Otherwise, the new node is appended to the end of the list
- The tail's next pointer is updated to point to the head (maintaining the circular structure)

### Insert First

Adds a new node at the beginning of the list.

```python
def insertFirst(self, data):
    # Implementation details...
```

**Parameters:**

- `data`: The value to store in the new node

**Behavior:**

- If the list is empty, the new node becomes both head and tail
- Otherwise, the new node is inserted at the beginning of the list
- The tail's next pointer is updated to point to the new head

### Delete Last

Removes the last node from the list.

```python
def deleteLast(self):
    # Implementation details...
```

**Behavior:**

- If the list is empty, the method returns without doing anything
- Otherwise, it removes the last node by updating the second-to-last node's next pointer
- Updates the tail reference to the new last node
- Prints the previous node's data

### Delete First

Removes the first node from the list.

```python
def deleteFirst(self):
    # Implementation details...
```

**Behavior:**

- If the list is empty, prints `False` and returns
- Otherwise, updates the head to the second node and updates the tail's next pointer

### Is Circle

Checks if the list is circular.

```python
def isCircle(self):
    # Implementation details...
```

**Behavior:**

- Traverses the list starting from the head
- If it reaches the head node again, prints `True` (indicating a circular list)
- Otherwise, prints `False`

### Traverse

Prints all elements in the list.

```python
def traverse(self):
    # Implementation details...
```

**Behavior:**

- If the list is empty, returns the string 'Empty'
- Otherwise, prints each node's data followed by '-> ' arrow
- Stops when it reaches the head node again (completes the full circle)

## Usage Example

```python
c = circle()

c.insert(1)
c.insert(2)
c.insert(3)
c.insert(4)
# c.insertFirst(12)
# c.deleteLast()
c.deleteFirst()
c.isCircle()
c.traverse()
```

This example:

1. Creates a new circular linked list
2. Inserts nodes with values 1, 2, 3, and 4
3. Deletes the first node (value 1)
4. Checks if the list is circular (prints True)
5. Traverses and prints all values in the list
