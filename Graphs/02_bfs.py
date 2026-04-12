"""
02 — BFS (Breadth-First Search)
================================
Explores level by level using a queue (FIFO).
Best for: shortest path in unweighted graphs, level-order traversal.
Time: O(V + E)  |  Space: O(V)
"""

from collections import deque


def bfs(graph, start):
    """
    Traverse the graph level by level.

    Args:
        graph: dict — adjacency list {vertex: [neighbors]}
        start: starting vertex

    Returns:
        list — visit order
    """
    visited = set([start])
    queue = deque([start])
    order = []

    while queue:
        vertex = queue.popleft()       # FIFO — take from the front
        order.append(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)  # add to the back

    return order


def bfs_with_levels(graph, start):
    """
    BFS that also tracks which level each node was discovered at.
    Useful for finding distances in unweighted graphs.

    Returns:
        dict — {vertex: level_number}
    """
    visited = set([start])
    queue = deque([(start, 0)])
    levels = {}

    while queue:
        vertex, level = queue.popleft()
        levels[vertex] = level

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, level + 1))

    return levels


# ── Demo ──
if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }

    print("Graph:")
    for v, neighbors in sorted(graph.items()):
        print(f"  {v} → {neighbors}")

    print(f"\nBFS from A: {bfs(graph, 'A')}")

    print("\nBFS with levels from A:")
    levels = bfs_with_levels(graph, "A")
    for vertex, level in sorted(levels.items()):
        print(f"  {vertex}: level {level}")
