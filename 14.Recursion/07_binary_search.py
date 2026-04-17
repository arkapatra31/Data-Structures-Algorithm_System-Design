"""
Divide & Conquer: Binary Search
=================================
Halve the search space each step. The recursive version makes
the divide-and-conquer nature explicit.

Time Complexity:  O(log n)
Space Complexity: O(log n) recursive, O(1) iterative
"""


def binary_search(arr: list, target: int, lo: int = 0, hi: int = None) -> int:
    """
    Find target in sorted array. Returns index or -1.
    Each recursive call eliminates half the remaining elements.
    """
    if hi is None:
        hi = len(arr) - 1

    # Base case: search space is empty
    if lo > hi:
        return -1

    mid = (lo + hi) // 2

    if arr[mid] == target:
        return mid                                    # found it
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, hi)  # search right half
    else:
        return binary_search(arr, target, lo, mid - 1)  # search left half


def binary_search_iterative(arr: list, target: int) -> int:
    """Iterative version — O(1) space."""
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


# ── Variants ─────────────────────────────────────────────────
def find_first(arr: list, target: int, lo: int = 0, hi: int = None) -> int:
    """Find the FIRST occurrence of target in sorted array."""
    if hi is None:
        hi = len(arr) - 1
    if lo > hi:
        return -1

    mid = (lo + hi) // 2
    # If found, check if it's the first occurrence
    if arr[mid] == target and (mid == 0 or arr[mid - 1] != target):
        return mid
    elif arr[mid] >= target:
        return find_first(arr, target, lo, mid - 1)
    else:
        return find_first(arr, target, mid + 1, hi)


def find_last(arr: list, target: int, lo: int = 0, hi: int = None) -> int:
    """Find the LAST occurrence of target in sorted array."""
    if hi is None:
        hi = len(arr) - 1
    if lo > hi:
        return -1

    mid = (lo + hi) // 2
    if arr[mid] == target and (mid == len(arr) - 1 or arr[mid + 1] != target):
        return mid
    elif arr[mid] <= target:
        return find_last(arr, target, mid + 1, hi)
    else:
        return find_last(arr, target, lo, mid - 1)


def search_rotated(arr: list, target: int, lo: int = 0, hi: int = None) -> int:
    """Binary search in a rotated sorted array (e.g., [4,5,6,7,0,1,2])."""
    if hi is None:
        hi = len(arr) - 1
    if lo > hi:
        return -1

    mid = (lo + hi) // 2
    if arr[mid] == target:
        return mid

    # Determine which half is sorted
    if arr[lo] <= arr[mid]:  # left half is sorted
        if arr[lo] <= target < arr[mid]:
            return search_rotated(arr, target, lo, mid - 1)
        else:
            return search_rotated(arr, target, mid + 1, hi)
    else:  # right half is sorted
        if arr[mid] < target <= arr[hi]:
            return search_rotated(arr, target, mid + 1, hi)
        else:
            return search_rotated(arr, target, lo, mid - 1)


# ── Demo ──────────────────────────────────────────────────────
if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    print(f"Array: {arr}")

    for target in [7, 12, 1, 19]:
        idx = binary_search(arr, target)
        status = f"found at index {idx}" if idx != -1 else "not found"
        print(f"  Search({target}): {status}")

    # Duplicates
    dup_arr = [1, 2, 2, 2, 3, 4, 4, 5]
    print(f"\nDuplicate array: {dup_arr}")
    print(f"  First 2: index {find_first(dup_arr, 2)}")
    print(f"  Last 2:  index {find_last(dup_arr, 2)}")

    # Rotated array
    rotated = [4, 5, 6, 7, 0, 1, 2]
    print(f"\nRotated array: {rotated}")
    for t in [0, 5, 3]:
        idx = search_rotated(rotated, t)
        status = f"found at index {idx}" if idx != -1 else "not found"
        print(f"  Search({t}): {status}")
