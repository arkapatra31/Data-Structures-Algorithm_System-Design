"""
Trees in DSA — 8. Segment Tree
Answers range queries (sum, min, max) in O(log n)
with O(log n) point updates.

Each node stores the answer for a range.
Children split that range in half.

Build: O(n)  |  Query: O(log n)  |  Update: O(log n)  |  Space: O(4n)
"""


class SegmentTree:
    """Segment tree for range sum queries with point updates."""

    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        if self.n > 0:
            self._build(arr, 0, 0, self.n - 1)

    def _build(self, arr, node, start, end):
        """Build tree recursively — each leaf is an array element."""
        if start == end:
            self.tree[node] = arr[start]
            return
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        self._build(arr, left_child, start, mid)
        self._build(arr, right_child, mid + 1, end)
        self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def update(self, idx, val, node=0, start=0, end=None):
        """Point update: set arr[idx] = val."""
        if end is None:
            end = self.n - 1
        if start == end:
            self.tree[node] = val
            return
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        if idx <= mid:
            self.update(idx, val, left_child, start, mid)
        else:
            self.update(idx, val, right_child, mid + 1, end)
        self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def query(self, l, r, node=0, start=0, end=None):
        """Range sum query: sum(arr[l..r]) inclusive."""
        if end is None:
            end = self.n - 1
        if r < start or end < l:        # no overlap
            return 0
        if l <= start and end <= r:      # total overlap
            return self.tree[node]
        mid = (start + end) // 2         # partial overlap
        left_sum = self.query(l, r, 2 * node + 1, start, mid)
        right_sum = self.query(l, r, 2 * node + 2, mid + 1, end)
        return left_sum + right_sum


class SegmentTreeMin:
    """Segment tree for range minimum queries."""

    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [float('inf')] * (4 * self.n)
        if self.n > 0:
            self._build(arr, 0, 0, self.n - 1)

    def _build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
            return
        mid = (start + end) // 2
        self._build(arr, 2 * node + 1, start, mid)
        self._build(arr, 2 * node + 2, mid + 1, end)
        self.tree[node] = min(self.tree[2 * node + 1],
                              self.tree[2 * node + 2])

    def update(self, idx, val, node=0, start=0, end=None):
        if end is None:
            end = self.n - 1
        if start == end:
            self.tree[node] = val
            return
        mid = (start + end) // 2
        if idx <= mid:
            self.update(idx, val, 2 * node + 1, start, mid)
        else:
            self.update(idx, val, 2 * node + 2, mid + 1, end)
        self.tree[node] = min(self.tree[2 * node + 1],
                              self.tree[2 * node + 2])

    def query(self, l, r, node=0, start=0, end=None):
        """Range minimum query: min(arr[l..r])."""
        if end is None:
            end = self.n - 1
        if r < start or end < l:
            return float('inf')
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        return min(
            self.query(l, r, 2 * node + 1, start, mid),
            self.query(l, r, 2 * node + 2, mid + 1, end)
        )


class LazySegmentTree:
    """
    Segment tree with lazy propagation — supports range updates.
    Range update + range query both in O(log n).
    """

    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        if self.n > 0:
            self._build(arr, 0, 0, self.n - 1)

    def _build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
            return
        mid = (start + end) // 2
        self._build(arr, 2 * node + 1, start, mid)
        self._build(arr, 2 * node + 2, mid + 1, end)
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def _propagate(self, node, start, end):
        """Push lazy updates down to children."""
        if self.lazy[node] != 0:
            self.tree[node] += self.lazy[node] * (end - start + 1)
            if start != end:
                self.lazy[2 * node + 1] += self.lazy[node]
                self.lazy[2 * node + 2] += self.lazy[node]
            self.lazy[node] = 0

    def range_update(self, l, r, val, node=0, start=0, end=None):
        """Add val to every element in arr[l..r]."""
        if end is None:
            end = self.n - 1
        self._propagate(node, start, end)
        if r < start or end < l:
            return
        if l <= start and end <= r:
            self.lazy[node] += val
            self._propagate(node, start, end)
            return
        mid = (start + end) // 2
        self.range_update(l, r, val, 2 * node + 1, start, mid)
        self.range_update(l, r, val, 2 * node + 2, mid + 1, end)
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query(self, l, r, node=0, start=0, end=None):
        """Range sum query with lazy propagation."""
        if end is None:
            end = self.n - 1
        self._propagate(node, start, end)
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        return (self.query(l, r, 2 * node + 1, start, mid) +
                self.query(l, r, 2 * node + 2, mid + 1, end))


# --- Demo ---
if __name__ == "__main__":
    arr = [3, 5, 7, 4, 8, 9]

    # Range Sum
    st = SegmentTree(arr)
    print("=== Range Sum Segment Tree ===")
    print(f"Array: {arr}")
    print(f"sum(1..4) = {st.query(1, 4)}")  # 5+7+4+8 = 24
    print(f"sum(0..5) = {st.query(0, 5)}")  # 36

    st.update(2, 10)  # arr[2] = 10
    print(f"After arr[2]=10: sum(1..4) = {st.query(1, 4)}")  # 5+10+4+8 = 27

    # Range Min
    stm = SegmentTreeMin(arr)
    print(f"\n=== Range Min Segment Tree ===")
    print(f"min(1..4) = {stm.query(1, 4)}")  # 4

    # Lazy propagation
    lst = LazySegmentTree([1, 2, 3, 4, 5])
    print(f"\n=== Lazy Segment Tree ===")
    print(f"sum(0..4) = {lst.query(0, 4)}")  # 15
    lst.range_update(1, 3, 10)  # add 10 to arr[1..3]
    print(f"After adding 10 to [1..3]: sum(0..4) = {lst.query(0, 4)}")  # 45
