"""
Divide & Conquer: Merge Sort
==============================
The textbook divide-and-conquer algorithm.
    1. DIVIDE:   Split array in half
    2. CONQUER:  Recursively sort each half
    3. COMBINE:  Merge the two sorted halves

Time Complexity:  O(n log n) — always
Space Complexity: O(n) — for the merge step
"""


def merge_sort(arr: list) -> list:
    """Sort array using merge sort. Returns a new sorted list."""
    # Base case: 0 or 1 elements are already sorted
    if len(arr) <= 1:
        return arr

    # Divide
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Combine
    return merge(left, right)


def merge(left: list, right: list) -> list:
    """Merge two sorted lists into one sorted list."""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# ── In-place version (more memory efficient) ─────────────────
def merge_sort_inplace(arr: list, left: int = 0, right: int = None):
    """Sort array in-place using merge sort."""
    if right is None:
        right = len(arr) - 1

    if left >= right:
        return

    mid = (left + right) // 2
    merge_sort_inplace(arr, left, mid)
    merge_sort_inplace(arr, mid + 1, right)
    merge_inplace(arr, left, mid, right)


def merge_inplace(arr: list, left: int, mid: int, right: int):
    """Merge two sorted subarrays in-place using a temp array."""
    temp = arr[left:right + 1]
    i = 0                    # pointer for left half in temp
    j = mid - left + 1       # pointer for right half in temp
    k = left                 # pointer for original array

    left_end = mid - left + 1
    right_end = right - left + 1

    while i < left_end and j < right_end:
        if temp[i] <= temp[j]:
            arr[k] = temp[i]
            i += 1
        else:
            arr[k] = temp[j]
            j += 1
        k += 1

    while i < left_end:
        arr[k] = temp[i]
        i += 1
        k += 1

    while j < right_end:
        arr[k] = temp[j]
        j += 1
        k += 1


# ── Visualization helper ─────────────────────────────────────
def merge_sort_verbose(arr: list, depth: int = 0) -> list:
    """Merge sort with step-by-step output."""
    indent = "  " * depth
    print(f"{indent}sort({arr})")

    if len(arr) <= 1:
        print(f"{indent}  → base case: {arr}")
        return arr

    mid = len(arr) // 2
    left = merge_sort_verbose(arr[:mid], depth + 1)
    right = merge_sort_verbose(arr[mid:], depth + 1)
    result = merge(left, right)
    print(f"{indent}  merge({left}, {right}) → {result}")
    return result


# ── Demo ──────────────────────────────────────────────────────
if __name__ == "__main__":
    data = [38, 27, 43, 3, 9, 82, 10]

    print("=== Merge Sort Trace ===")
    sorted_data = merge_sort_verbose(data)
    print(f"\nOriginal: {data}")
    print(f"Sorted:   {sorted_data}")

    print("\n=== In-place Merge Sort ===")
    data2 = [5, 2, 8, 1, 9, 3, 7, 4, 6]
    print(f"Before: {data2}")
    merge_sort_inplace(data2)
    print(f"After:  {data2}")
