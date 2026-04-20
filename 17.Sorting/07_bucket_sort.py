"""
Bucket Sort
===========
A distribution-based sorting algorithm that distributes elements
into a number of "buckets", sorts each bucket individually,
then concatenates them back together in order.

Best for uniformly distributed data over a known range.

Time:  Best O(n + k) | Avg O(n + k) | Worst O(n²) — all in one bucket
Space: O(n + k) — buckets need extra memory
Stable: Yes (when using a stable sort for individual buckets)

Where k = number of buckets.
"""

# Shared test array (same across all sorting files)
arr = [38, 27, 43, 3, 9, 82, 10]


def bucket_sort(arr: list, num_buckets: int = 5) -> list:
    if not arr:
        return arr[:]

    a = arr[:]
    min_val, max_val = min(a), max(a)

    # Edge case: all elements are the same
    if min_val == max_val:
        return a

    # Each bucket covers an equal slice of the value range
    bucket_range = (max_val - min_val + 1) / num_buckets

    # Step 1: Create empty buckets
    buckets = [[] for _ in range(num_buckets)]

    # Step 2: Distribute elements into buckets
    for val in a:
        idx = int((val - min_val) / bucket_range)
        if idx == num_buckets:   # max_val edge case
            idx -= 1
        buckets[idx].append(val)

    # Step 3: Sort each individual bucket
    # Using Python's built-in sort (Timsort) here,
    # but insertion sort is the classic choice for small buckets
    for bucket in buckets:
        bucket.sort()

    # Step 4: Concatenate all sorted buckets
    result = []
    for bucket in buckets:
        result.extend(bucket)

    return result


if __name__ == "__main__":
    print(f"Original : {arr}")
    print(f"Sorted   : {bucket_sort(arr)}")
    # Output: [3, 9, 10, 27, 38, 43, 82]
