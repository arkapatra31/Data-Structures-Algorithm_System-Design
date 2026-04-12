"""
04 — Shortest Path (BFS — Unweighted Graphs)
==============================================
In an unweighted graph, BFS naturally finds the shortest path because
it explores nodes level by level — the first time it reaches a node
is always via the shortest route.
Time: O(V + E)  |  Space: O(V)
"""

from collections import deque


def shortest_path_bfs(graph, start, end):
    """
    Find the shortest path in an UNWEIGHTED graph.

    Args:
        graph: dict — adjacency list {vertex: [neighbors]}
        start: source vertex
        end: destination vertex

    Returns:
        list — shortest path, or None if no path exists
    """
    if start == end:
        return [start]

    visited = set([start])
    queue = deque([(start, [start])])  # (current_node, path_so_far)

    while queue:
        vertex, path = queue.popleft()

        for neighbor in graph[vertex]:
            if neighbor == end:
                return path + [neighbor]  # found shortest path!

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None  # no path exists


def all_shortest_distances(graph, start):
    """
    Find shortest distance from start to ALL reachable vertices.

    Returns:
        dict — {vertex: distance} (-1 if unreachable)
    """
    distances = {v: -1 for v in graph}
    distances[start] = 0

    visited = set([start])
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                distances[neighbor] = distances[vertex] + 1
                queue.append(neighbor)

    return distances


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

    # Shortest path
    path = shortest_path_bfs(graph, "A", "F")
    print(f"\nShortest path A → F: {' → '.join(path)}")

    path2 = shortest_path_bfs(graph, "D", "F")
    print(f"Shortest path D → F: {' → '.join(path2)}")

    # All distances
    print("\nDistances from A:")
    distances = all_shortest_distances(graph, "A")
    for vertex, dist in sorted(distances.items()):
        print(f"  A → {vertex} = {dist} edge(s)")
