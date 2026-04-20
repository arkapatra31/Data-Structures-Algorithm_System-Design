"""
Merge Sort
==========
Divide-and-conquer: recursively split the array in half,
sort each half, then merge the sorted halves back together.

Time:  Best O(n log n) | Avg O(n log n) | Worst O(n log n)
Space: O(n) — needs temporary arrays for merging
Stable: Yes
"""

# Shared test array (same across all sorting files)
arr = [38, 27, 43, 3, 9, 82, 10]


def merge_sort(arr: list) -> list:
    # Base case: single element or empty
    if len(arr) <= 1:
        return arr[:]

    mid = len(arr) // 2

    # Recursively sort each half
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge the two sorted halves
    return _merge(left, right)


def _merge(left: list, right: list) -> list:
    """Merge two sorted lists into one sorted list."""
    result = []
    i = j = 0

    # Compare front elements and pick the smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:   # <= preserves stability
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result


if __name__ == "__main__":
    print(f"Original : {arr}")
    print(f"Sorted   : {merge_sort(arr)}")
    # Output: [3, 9, 10, 27, 38, 43, 82]
