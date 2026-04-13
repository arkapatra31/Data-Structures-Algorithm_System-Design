"""
03 — DFS (Depth-First Search)
==============================
Dives as deep as possible before backtracking, using a stack (LIFO).
Best for: cycle detection, topological sort, pathfinding, maze solving.
Time: O(V + E)  |  Space: O(V)
"""


def dfs_iterative(graph, start):
    """
    Iterative DFS using an explicit stack.
    Safer than recursive for large graphs (no stack overflow).

    Args:
        graph: dict — adjacency list {vertex: [neighbors]}
        start: starting vertex

    Returns:
        list — visit order
    """

    visited = set([start])
    stack = [start]
    order = []
    while stack:
        vertex = stack.pop()           # LIFO — take from the top
        order.append(vertex)

        for neighbor in reversed(graph[vertex]):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

    return order


def dfs_recursive(graph, vertex, visited=None, order=None):
    """
    Recursive DFS — elegant but risks stack overflow on huge graphs.

    Args:
        graph: dict — adjacency list
        vertex: current vertex
        visited: set of visited vertices (auto-created on first call)
        order: accumulator list (auto-created on first call)

    Returns:
        list — visit order
    """
    if visited is None:
        visited = set()
        order = []

    visited.add(vertex)
    order.append(vertex)

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, order)

    return order


def dfs_path_exists(graph, start, end):
    """Check if a path exists between two vertices using DFS."""
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex == end:
            return True
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    stack.append(neighbor)

    return False


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

    print(f"\nDFS iterative from A: {dfs_iterative(graph, 'A')}")
    print(f"DFS recursive from A: {dfs_recursive(graph, 'A')}")
    print(f"\nPath exists A → F? {dfs_path_exists(graph, 'A', 'F')}")
    print(f"Path exists A → Z? {dfs_path_exists(graph, 'A', 'Z') if 'Z' in graph else False}")
