"""
Bubble Sort
===========
Repeatedly swap adjacent elements if they're in the wrong order.
Each pass bubbles the largest unsorted element to the end.

Time:  Best O(n) | Avg O(n²) | Worst O(n²)
Space: O(1) — in-place
Stable: Yes
"""

# Shared test array (same across all sorting files)
arr = [38, 27, 43, 3, 9, 82, 10]


def bubble_sort(arr: list) -> list:
    a = arr[:]  # work on a copy to preserve original
    n = len(a)

    for i in range(n):
        swapped = False  # early-exit optimization

        # After each pass, the last i elements are already sorted
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                # Swap adjacent elements
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True

        # If no swaps happened, array is already sorted
        if not swapped:
            break

    return a


if __name__ == "__main__":
    print(f"Original : {arr}")
    print(f"Sorted   : {bubble_sort(arr)}")
    # Output: [3, 9, 10, 27, 38, 43, 82]
