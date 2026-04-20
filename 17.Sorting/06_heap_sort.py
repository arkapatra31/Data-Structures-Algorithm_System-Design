"""
Heap Sort
=========
Builds a max-heap from the array, then repeatedly extracts
the maximum (root) and places it at the end of the sorted portion.

Time:  Best O(n log n) | Avg O(n log n) | Worst O(n log n)
Space: O(1) — in-place
Stable: No

Heap property:  parent >= both children
Index math:     left child = 2i + 1,  right child = 2i + 2
"""

# Shared test array (same across all sorting files)
arr = [38, 27, 43, 3, 9, 82, 10]


def heap_sort(arr: list) -> list:
    a = arr[:]
    n = len(a)

    # Phase 1: Build max-heap (bottom-up from last non-leaf)
    for i in range(n // 2 - 1, -1, -1):
        _heapify(a, n, i)

    # Phase 2: Extract max one by one
    for i in range(n - 1, 0, -1):
        # Move current root (max) to the end
        a[0], a[i] = a[i], a[0]
        # Restore heap property on the reduced heap
        _heapify(a, i, 0)

    return a


def _heapify(a: list, heap_size: int, root: int):
    """Push the root down until max-heap property is restored."""
    largest = root
    left = 2 * root + 1
    right = 2 * root + 2

    if left < heap_size and a[left] > a[largest]:
        largest = left
    if right < heap_size and a[right] > a[largest]:
        largest = right

    if largest != root:
        a[root], a[largest] = a[largest], a[root]
        _heapify(a, heap_size, largest)   # recurse on the affected subtree


if __name__ == "__main__":
    print(f"Original : {arr}")
    print(f"Sorted   : {heap_sort(arr)}")
    # Output: [3, 9, 10, 27, 38, 43, 82]
