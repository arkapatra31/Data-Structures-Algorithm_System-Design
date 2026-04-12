"""
05 — Dijkstra's Algorithm (Weighted Shortest Path)
====================================================
Finds shortest distances from a source to ALL other vertices in a
weighted graph with non-negative edge weights.
Uses a min-heap (priority queue) to always process the closest vertex next.
Time: O((V + E) log V)  |  Space: O(V)
"""

import heapq


def dijkstra(graph, start):
    """
    Compute shortest distances from start to all vertices.

    Args:
        graph: dict — {vertex: [(neighbor, weight), ...]}
        start: source vertex

    Returns:
        (distances, previous) — dicts for reconstruction
    """
    distances = {v: float('inf') for v in graph}
    distances[start] = 0
    previous = {v: None for v in graph}
    min_heap = [(0, start)]  # (distance, vertex)

    while min_heap:
        current_dist, current = heapq.heappop(min_heap)

        # Skip if we already found a better path
        if current_dist > distances[current]:
            continue

        for neighbor, weight in graph[current]:
            distance = current_dist + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current
                heapq.heappush(min_heap, (distance, neighbor))

    return distances, previous


def reconstruct_path(previous, start, end):
    """Trace back from end to start using the previous dict."""
    if previous.get(end) is None and end != start:
        return None  # unreachable

    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()

    return path if path[0] == start else None


def dijkstra_path(graph, start, end):
    """Convenience: get shortest path + cost in one call."""
    distances, previous = dijkstra(graph, start)

    if distances[end] == float('inf'):
        return None, float('inf')

    path = reconstruct_path(previous, start, end)
    return path, distances[end]


# ── Demo ──
if __name__ == "__main__":
    # Weighted graph as adjacency list of (neighbor, weight) tuples
    graph = {
        "A": [("B", 4), ("C", 2)],
        "B": [("A", 4), ("D", 3), ("E", 1), ("C", 1)],
        "C": [("A", 2), ("B", 1), ("D", 5)],
        "D": [("B", 3), ("C", 5), ("E", 2)],
        "E": [("B", 1), ("D", 2)],
    }

    print("Weighted Graph:")
    for v, edges in sorted(graph.items()):
        neighbors = ", ".join(f"{n}(w={w})" for n, w in edges)
        print(f"  {v} → [{neighbors}]")

    # All distances
    distances, _ = dijkstra(graph, "A")
    print("\nDijkstra from A (shortest distances):")
    for vertex, dist in sorted(distances.items()):
        print(f"  A → {vertex} = {dist}")

    # Specific path
    path, cost = dijkstra_path(graph, "A", "E")
    print(f"\nShortest path A → E:")
    print(f"  Path: {' → '.join(path)}")
    print(f"  Cost: {cost}")

    path2, cost2 = dijkstra_path(graph, "A", "D")
    print(f"\nShortest path A → D:")
    print(f"  Path: {' → '.join(path2)}")
    print(f"  Cost: {cost2}")
