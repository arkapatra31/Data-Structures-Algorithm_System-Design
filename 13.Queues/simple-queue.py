class SimpleQueue:
    """FIFO Queue — elements enter at rear, exit from front."""

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        """Add item to the rear of the queue."""
        self.items.append(item)
        print(f"  Enqueued: {item} | Queue: {self.items}")

    def dequeue(self):
        """Remove and return item from the front."""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        item = self.items.pop(0)
        print(f"  Dequeued: {item} | Queue: {self.items}")
        return item

    def peek(self):
        """Return front item without removing it."""
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.items[0]

    def size(self):
        return len(self.items)

    def __repr__(self):
        return f"SimpleQueue({self.items})"


# --- Demo ---
if __name__ == "__main__":
    print("=== Simple Queue Demo ===\n")
    q = SimpleQueue()

    print("Enqueue operations:")
    for val in [10, 20, 30, 40, 50]:
        q.enqueue(val)

    print(f"\nFront element (peek): {q.peek()}")
    print(f"Queue size: {q.size()}\n")

    print("Dequeue operations:")
    q.dequeue()
    q.dequeue()

    print(f"\nFinal state: {q}")
