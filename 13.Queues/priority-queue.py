import heapq


class PriorityQueue:
    """Min-priority queue using a binary heap.
    Lower priority number = higher urgency (served first).
    """

    def __init__(self):
        self._heap = []
        self._index = 0  # tiebreaker for same-priority items

    def is_empty(self):
        return len(self._heap) == 0

    def enqueue(self, item, priority):
        """Add item with a given priority (lower = more urgent)."""
        heapq.heappush(self._heap, (priority, self._index, item))
        self._index += 1
        print(f"  Enqueued: '{item}' with priority {priority}")

    def dequeue(self):
        """Remove and return the highest-priority (lowest number) item."""
        if self.is_empty():
            raise IndexError("Dequeue from empty priority queue")
        priority, _, item = heapq.heappop(self._heap)
        print(f"  Dequeued: '{item}' (priority {priority})")
        return item

    def peek(self):
        """Return highest-priority item without removing it."""
        if self.is_empty():
            raise IndexError("Peek from empty priority queue")
        priority, _, item = self._heap[0]
        return item, priority

    def size(self):
        return len(self._heap)

    def __repr__(self):
        sorted_items = sorted(self._heap)
        return "PriorityQueue([" + ", ".join(
            f"('{item}', p={p})" for p, _, item in sorted_items
        ) + "])"


# --- Demo ---
if __name__ == "__main__":
    print("=== Priority Queue Demo ===\n")
    pq = PriorityQueue()

    print("Enqueue tasks (lower number = higher priority):")
    pq.enqueue("Send email", priority=3)
    pq.enqueue("Fix critical bug", priority=1)
    pq.enqueue("Write report", priority=2)
    pq.enqueue("Update docs", priority=4)
    pq.enqueue("Deploy hotfix", priority=1)

    print(f"\nNext up (peek): {pq.peek()}")
    print(f"Queue size: {pq.size()}\n")

    print("Dequeue all (served by priority):")
    while not pq.is_empty():
        pq.dequeue()

    # --- Practical use: Hospital triage ---
    print("\n=== Practical: Hospital Emergency Triage ===")
    er = PriorityQueue()
    patients = [
        ("Mild headache", 5),
        ("Cardiac arrest", 1),
        ("Broken arm", 3),
        ("Severe bleeding", 2),
        ("Sprained ankle", 4),
    ]
    print("\nPatients arrive:")
    for name, severity in patients:
        er.enqueue(name, severity)

    print("\nTreatment order:")
    while not er.is_empty():
        er.dequeue()
