class Deque:
    """Double-ended queue — insert/delete at both front and rear."""

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def insert_front(self, item):
        """Add item at the front."""
        self.items.insert(0, item)
        print(f"  Insert front: {item} | Deque: {self.items}")

    def insert_rear(self, item):
        """Add item at the rear."""
        self.items.append(item)
        print(f"  Insert rear:  {item} | Deque: {self.items}")

    def delete_front(self):
        """Remove and return item from front."""
        if self.is_empty():
            raise IndexError("Delete from empty deque")
        item = self.items.pop(0)
        print(f"  Delete front: {item} | Deque: {self.items}")
        return item

    def delete_rear(self):
        """Remove and return item from rear."""
        if self.is_empty():
            raise IndexError("Delete from empty deque")
        item = self.items.pop()
        print(f"  Delete rear:  {item} | Deque: {self.items}")
        return item

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Peek from empty deque")
        return self.items[0]

    def peek_rear(self):
        if self.is_empty():
            raise IndexError("Peek from empty deque")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __repr__(self):
        return f"Deque({self.items})"


# --- Demo ---
if __name__ == "__main__":
    print("=== Deque Demo ===\n")
    dq = Deque()

    print("Insert operations:")
    dq.insert_rear(10)
    dq.insert_rear(20)
    dq.insert_front(5)
    dq.insert_rear(30)
    dq.insert_front(1)

    print(f"\nFront: {dq.peek_front()}, Rear: {dq.peek_rear()}")
    print(f"Size: {dq.size()}\n")

    print("Delete operations:")
    dq.delete_front()
    dq.delete_rear()

    print(f"\nFinal state: {dq}")

    # --- Practical use: Sliding window maximum ---
    print("\n=== Practical: Sliding Window Max (k=3) ===")
    from collections import deque

    def sliding_window_max(nums, k):
        """Find maximum in each window of size k using a deque."""
        dq = deque()  # stores indices
        result = []
        for i, num in enumerate(nums):
            while dq and dq[0] < i - k + 1:
                dq.popleft()
            while dq and nums[dq[-1]] < num:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                result.append(nums[dq[0]])
        return result

    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    print(f"Array: {nums}")
    print(f"Window maxes (k=3): {sliding_window_max(nums, 3)}")
