"""
07 — Topological Sort (Kahn's Algorithm)
==========================================
Orders vertices in a DAG so that for every edge u→v, u comes before v.
Uses BFS with in-degree tracking (Kahn's algorithm).

Use cases: build systems, course prerequisites, package managers, spreadsheets.
Time: O(V + E)  |  Space: O(V)
"""

from collections import deque


def topological_sort_kahn(graph):
    """
    Kahn's algorithm — BFS-based topological sort.

    Args:
        graph: dict — {vertex: [neighbors]}  (directed)

    Returns:
        list — topologically sorted vertices

    Raises:
        ValueError — if graph has a cycle
    """
    # Step 1: Calculate in-degrees
    in_degree = {v: 0 for v in graph}
    for v in graph:
        for neighbor in graph[v]:
            in_degree[neighbor] += 1

    # Step 2: Enqueue all vertices with in-degree 0
    queue = deque([v for v in in_degree if in_degree[v] == 0])
    order = []

    # Step 3: Process
    while queue:
        vertex = queue.popleft()
        order.append(vertex)

        for neighbor in graph[vertex]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Step 4: Check for cycle
    if len(order) != len(graph):
        raise ValueError("Graph has a cycle — topological sort impossible!")

    return order


def topological_sort_dfs(graph):
    """
    DFS-based topological sort — alternative approach.
    Adds vertices to result in reverse post-order.

    Returns:
        list — topologically sorted vertices
    """
    visited = set()
    result = []

    def _dfs(vertex):
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                _dfs(neighbor)
        result.append(vertex)  # add AFTER all descendants

    for vertex in graph:
        if vertex not in visited:
            _dfs(vertex)

    result.reverse()  # reverse post-order = topological order
    return result


# ── Demo ──
if __name__ == "__main__":
    # Course prerequisites
    courses = {
        "Math":          ["Physics", "Stats"],
        "Physics":       ["Quantum", "ML"],
        "Stats":         ["ML"],
        "Quantum":       [],
        "ML":            ["Deep Learning"],
        "Deep Learning": [],
    }

    print("Course prerequisite graph:")
    for v, deps in sorted(courses.items()):
        print(f"  {v} → {deps if deps else '(none)'}")

    print(f"\nKahn's algorithm: {topological_sort_kahn(courses)}")
    print(f"DFS-based:        {topological_sort_dfs(courses)}")

    # Build system example
    build = {
        "parse":    ["compile"],
        "compile":  ["link"],
        "lint":     ["compile"],
        "link":     ["deploy"],
        "test":     ["deploy"],
        "deploy":   [],
    }

    print(f"\nBuild pipeline order: {topological_sort_kahn(build)}")
