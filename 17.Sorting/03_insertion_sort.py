"""
Insertion Sort
==============
Builds the sorted array one element at a time by picking each
element and inserting it into its correct position among the
already-sorted elements — like sorting playing cards in your hand.

Time:  Best O(n) | Avg O(n²) | Worst O(n²)
Space: O(1) — in-place
Stable: Yes
"""

# Shared test array (same across all sorting files)
arr = [38, 27, 43, 3, 9, 82, 10]


def insertion_sort(arr: list) -> list:
    a = arr[:]

    for i in range(1, len(a)):
        key = a[i]   # the element we need to insert
        j = i - 1

        # Shift elements in the sorted region rightward
        # to make room for the key
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1

        # Insert the key into the gap
        a[j + 1] = key

    return a


if __name__ == "__main__":
    print(f"Original : {arr}")
    print(f"Sorted   : {insertion_sort(arr)}")
    # Output: [3, 9, 10, 27, 38, 43, 82]
