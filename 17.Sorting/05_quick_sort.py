"""
Quick Sort
==========
Choose a pivot, partition so elements < pivot go left and
elements >= pivot go right, then recurse on each partition.
Uses the Lomuto partition scheme (pivot = last element).

Time:  Best O(n log n) | Avg O(n log n) | Worst O(n²)
Space: O(log n) — call stack depth
Stable: No
"""

# Shared test array (same across all sorting files)
arr = [38, 27, 43, 3, 9, 82, 10]


def quick_sort(arr: list) -> list:
    a = arr[:]
    _quick_sort_helper(a, 0, len(a) - 1)
    return a


def _quick_sort_helper(a: list, low: int, high: int):
    if low < high:
        pivot_idx = _partition(a, low, high)
        _quick_sort_helper(a, low, pivot_idx - 1)    # left of pivot
        _quick_sort_helper(a, pivot_idx + 1, high)    # right of pivot


def _partition(a: list, low: int, high: int) -> int:
    """Lomuto partition: pivot is the last element."""
    pivot = a[high]
    i = low  # boundary of the "less than pivot" region

    for j in range(low, high):
        if a[j] < pivot:
            a[i], a[j] = a[j], a[i]   # swap into the left region
            i += 1

    # Place pivot in its final sorted position
    a[i], a[high] = a[high], a[i]
    return i


if __name__ == "__main__":
    print(f"Original : {arr}")
    print(f"Sorted   : {quick_sort(arr)}")
    # Output: [3, 9, 10, 27, 38, 43, 82]
