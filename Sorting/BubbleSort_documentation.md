# Bubble Sort Implementation

This document provides documentation for the bubble sort algorithm implementation in `BubbleSort.py`.

## Algorithm Overview

Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The algorithm gets its name because smaller elements "bubble" to the top of the list with each iteration.

## Implementation

```python
def bubble(arr):
    for i in range(len(arr)-1):
        swap = False
        print("Main")
        for j in range(len(arr)-1-i):
            print("test")
            if arr[j] > arr[j+1]:
               arr[j], arr[j+1] = arr[j+1], arr[j]
               swap = True
        if not swap:
            break
    return arr
```

## Function Details

### Parameters

- `arr`: The array/list to be sorted

### Return Value

- The sorted array

### Time Complexity

- Worst-case: O(n²) - when the array is reverse sorted
- Average-case: O(n²)
- Best-case: O(n) - when the array is already sorted (with the optimization included)

### Space Complexity

- O(1) - in-place sorting algorithm

## Key Features

1. **Early Termination**: The algorithm uses a `swap` flag to detect if any swaps were made in a pass. If no swaps were made, the array is already sorted, and the algorithm terminates early.

2. **Optimization**: With each pass, the largest unsorted element "bubbles" to its correct position at the end of the array. Therefore, each pass can examine one fewer element than the previous pass (using `len(arr)-1-i` in the inner loop).

3. **Debugging Output**: The implementation includes `print` statements to track execution flow:
   - "Main" is printed at the start of each outer loop iteration
   - "test" is printed at the start of each inner loop iteration

## Usage Example

```python
arr = [1.1, 3.3, 5.5, 7.7, 2.2, 4.4, 6.6]
print(bubble(arr))
```

This example:

1. Creates an array of floating-point numbers
2. Calls the bubble sort function to sort the array
3. Prints the sorted result
