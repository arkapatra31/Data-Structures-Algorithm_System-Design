class CircularQueue:
    """Fixed-size queue that wraps rear pointer back to the start."""

    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = -1
        self.rear = -1
        self.count = 0

    def is_empty(self):
        """Check if the queue is empty."""
        return self.count == 0

    def is_full(self):
        """Check if the queue is full."""
        return self.count == self.capacity

    def enqueue(self, item):
        """Add item at rear; wraps around using modular arithmetic."""
        if self.is_full():
            raise OverflowError("Queue is full")
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.items[self.rear] = item
        self.count += 1
        print(f"  Enqueued: {item} | front={self.front}, rear={self.rear} | {self._snapshot()}")

    def dequeue(self):
        """Remove item from front; wraps around."""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        item = self.items[self.front]
        self.items[self.front] = None
        self.count -= 1
        if self.is_empty():
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        print(f"  Dequeued: {item} | front={self.front}, rear={self.rear} | {self._snapshot()}")
        return item

    def peek(self):
        """Get the front item without removing it."""
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.items[self.front]

    def _snapshot(self):
        """Get a snapshot of the queue's current state."""
        return [self.items[i] for i in range(self.capacity)]

    def __repr__(self):
        return f"CircularQueue(cap={self.capacity}, {self._snapshot()})"


# --- Demo ---
if __name__ == "__main__":
    print("=== Circular Queue Demo (capacity=5) ===\n")
    cq = CircularQueue(5)

    print("Enqueue 10, 20, 30, 40, 50:")
    for v in [10, 20, 30, 40, 50]:
        cq.enqueue(v)

    print("\nDequeue two items:")
    cq.dequeue()
    cq.dequeue()

    print("\nEnqueue 60, 70 (wraps around!):")
    cq.enqueue(60)
    cq.enqueue(70)

    print(f"\nFinal state: {cq}")
    print(f"Front element: {cq.peek()}")
