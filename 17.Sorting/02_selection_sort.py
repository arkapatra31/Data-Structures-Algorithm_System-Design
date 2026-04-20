"""
Selection Sort
==============
Find the minimum in the unsorted region, swap it to the front.
Divides the array into sorted (left) and unsorted (right).

Time:  Best O(n²) | Avg O(n²) | Worst O(n²)
Space: O(1) — in-place
Stable: No
"""

# Shared test array (same across all sorting files)
arr = [38, 27, 43, 3, 9, 82, 10]


def selection_sort(arr: list) -> list:
    a = arr[:]
    n = len(a)

    for i in range(n):
        min_idx = i

        # Scan the unsorted region for the minimum
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j

        # Swap minimum into the sorted region boundary
        a[i], a[min_idx] = a[min_idx], a[i]

    return a


if __name__ == "__main__":
    print(f"Original : {arr}")
    print(f"Sorted   : {selection_sort(arr)}")
    # Output: [3, 9, 10, 27, 38, 43, 82]
