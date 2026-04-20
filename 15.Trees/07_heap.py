"""
Trees in DSA — 7. Heap / Priority Queue
A complete binary tree stored as a flat array.
  - Max-heap: parent ≥ children
  - Min-heap: parent ≤ children

Array indexing (0-based):
  parent(i)     = (i - 1) // 2
  left_child(i) = 2 * i + 1
  right_child(i)= 2 * i + 2

Push: O(log n)  |  Pop: O(log n)  |  Peek: O(1)  |  Build: O(n)
"""


class MinHeap:
    """Min-heap from scratch — smallest element always at top."""

    def __init__(self):
        self.heap = []

    def push(self, val):
        """Append at the end, then heapify upward toward the root."""
        self.heap.append(val)
        self._heapify_insert(len(self.heap) - 1)

    def pop(self):
        """Remove root: save it, move last element to root, heapify downward."""
        if not self.heap:
            return None
        extracted = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self._heapify_extract(0)
        return extracted

    def peek(self):
        """View smallest without removing."""
        return self.heap[0] if self.heap else None

    def size(self):
        return len(self.heap)

    def _heapify_insert(self, index):
        """Recursively swap with parent while child is smaller."""
        if index <= 0:
            return
        parent = (index - 1) // 2
        if self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
        self._heapify_insert(parent)

    def _heapify_extract(self, index):
        """Recursively swap with smaller child. Three cases: no left child,
        only a left child, or both children (pick the smaller one)."""
        n = len(self.heap)
        left = 2 * index + 1
        right = 2 * index + 2

        if n <= left:
            return
        elif n == left + 1:
            if self.heap[index] > self.heap[left]:
                self.heap[index], self.heap[left] = self.heap[left], self.heap[index]
            return
        else:
            swap_child = left if self.heap[left] < self.heap[right] else right
            if self.heap[index] > self.heap[swap_child]:
                self.heap[index], self.heap[swap_child] = self.heap[swap_child], self.heap[index]
            self._heapify_extract(swap_child)


class MaxHeap:
    """Max-heap — largest element always at top."""

    def __init__(self):
        self.heap = []

    def push(self, val):
        self.heap.append(val)
        self._heapify_insert(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None
        extracted = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self._heapify_extract(0)
        return extracted

    def peek(self):
        return self.heap[0] if self.heap else None

    def size(self):
        return len(self.heap)

    def _heapify_insert(self, index):
        if index <= 0:
            return
        parent = (index - 1) // 2
        if self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
        self._heapify_insert(parent)

    def _heapify_extract(self, index):
        n = len(self.heap)
        left = 2 * index + 1
        right = 2 * index + 2

        if n <= left:
            return
        elif n == left + 1:
            if self.heap[index] < self.heap[left]:
                self.heap[index], self.heap[left] = self.heap[left], self.heap[index]
            return
        else:
            swap_child = left if self.heap[left] > self.heap[right] else right
            if self.heap[index] < self.heap[swap_child]:
                self.heap[index], self.heap[swap_child] = self.heap[swap_child], self.heap[index]
            self._heapify_extract(swap_child)


def heapify(arr):
    """Build a min-heap from array in O(n) — bottom-up approach."""
    n = len(arr)
    # Start from last non-leaf node and sift down each
    for i in range(n // 2 - 1, -1, -1):
        _sift_down_arr(arr, i, n)
    return arr


def _sift_down_arr(arr, i, n):
    while True:
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left] < arr[smallest]:
            smallest = left
        if right < n and arr[right] < arr[smallest]:
            smallest = right
        if smallest == i:
            break
        arr[i], arr[smallest] = arr[smallest], arr[i]
        i = smallest


def heap_sort(arr):
    """Sort array using heap — O(n log n)."""
    n = len(arr)
    # Build max-heap
    for i in range(n // 2 - 1, -1, -1):
        _sift_down_max(arr, i, n)
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        _sift_down_max(arr, 0, i)
    return arr


def _sift_down_max(arr, i, n):
    while True:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest == i:
            break
        arr[i], arr[largest] = arr[largest], arr[i]
        i = largest


# ============================================================
#  Using Python's built-in heapq (recommended in practice)
# ============================================================

def top_k_smallest(arr, k):
    """Find k smallest elements using heapq."""
    import heapq
    return heapq.nsmallest(k, arr)


def top_k_largest(arr, k):
    """Find k largest elements using heapq."""
    import heapq
    return heapq.nlargest(k, arr)


def merge_k_sorted_lists(lists):
    """Merge k sorted lists into one sorted list — classic heap problem."""
    import heapq
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    result = []
    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))

    return result


# --- Demo ---
if __name__ == "__main__":
    # Min-heap demo
    h = MinHeap()
    for v in [5, 3, 8, 1, 4, 9, 2]:
        h.push(v)

    print("Min-heap pop order:", end=" ")
    while h.size():
        print(h.pop(), end=" ")
    print()

    # Max-heap demo
    mh = MaxHeap()
    for v in [5, 3, 8, 1, 4]:
        mh.push(v)
    print(f"Max-heap peek: {mh.peek()}")

    # Heap sort
    arr = [5, 3, 8, 1, 4, 9, 2]
    print(f"Heap sort: {heap_sort(arr[:])}")

    # Top-K
    data = [10, 4, 3, 50, 23, 90, 1]
    print(f"Top 3 smallest: {top_k_smallest(data, 3)}")
    print(f"Top 3 largest:  {top_k_largest(data, 3)}")

    # Merge k sorted lists
    lists = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    print(f"Merged: {merge_k_sorted_lists(lists)}")
