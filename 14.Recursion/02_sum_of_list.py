"""
Recursion Basics: Sum of a List
================================
Demonstrates reducing a list problem by processing one element at a time.

Time Complexity:  O(n)
Space Complexity: O(n) — call stack + slicing creates copies
"""


def recursive_sum(arr: list) -> int:
    """Sum all elements recursively."""
    # Base case: empty list has sum 0
    if not arr:
        return 0
    # Recursive case: first element + sum of the rest
    return arr[0] + recursive_sum(arr[1:])


def recursive_sum_optimized(arr: list, index: int = 0) -> int:
    """Index-based version — avoids O(n) slicing cost per call."""
    if index >= len(arr):
        return 0
    return arr[index] + recursive_sum_optimized(arr, index + 1)


def recursive_max(arr: list) -> float:
    """Find the maximum element recursively."""
    if len(arr) == 1:
        return arr[0]
    sub_max = recursive_max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max


def recursive_count(arr: list, target) -> int:
    """Count occurrences of target in list."""
    if not arr:
        return 0
    match = 1 if arr[0] == target else 0
    return match + recursive_count(arr[1:], target)


# ── Demo ──────────────────────────────────────────────────────
if __name__ == "__main__":
    data = [3, 7, 1, 9, 4, 6]

    print(f"List: {data}")
    print(f"Sum:   {recursive_sum(data)}")
    print(f"Sum (optimized): {recursive_sum_optimized(data)}")
    print(f"Max:   {recursive_max(data)}")
    print(f"Count of 7: {recursive_count(data, 7)}")
    print(f"Count of 5: {recursive_count(data, 5)}")
