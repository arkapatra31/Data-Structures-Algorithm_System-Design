"""
06 — Cycle Detection (DFS Coloring)
=====================================
Detects whether a graph contains a cycle using the three-color DFS scheme:
  WHITE (0) = unvisited
  GRAY  (1) = currently being explored (in the recursion stack)
  BLACK (2) = fully processed

If we encounter a GRAY node during DFS, we've found a back edge → cycle!
Time: O(V + E)  |  Space: O(V)
"""


def has_cycle_directed(graph):
    """
    Detect cycle in a DIRECTED graph.

    Args:
        graph: dict — {vertex: [neighbors]}

    Returns:
        bool — True if cycle exists
    """
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {v: WHITE for v in graph}

    def _dfs(vertex):
        color[vertex] = GRAY

        for neighbor in graph[vertex]:
            if color[neighbor] == GRAY:
                return True                # back edge → cycle!
            if color[neighbor] == WHITE:
                if _dfs(neighbor):
                    return True

        color[vertex] = BLACK
        return False

    for vertex in graph:
        if color[vertex] == WHITE:
            if _dfs(vertex):
                return True
    return False


def has_cycle_undirected(graph):
    """
    Detect cycle in an UNDIRECTED graph.
    We track the parent to avoid counting the edge we came from as a cycle.

    Args:
        graph: dict — {vertex: [neighbors]}

    Returns:
        bool — True if cycle exists
    """
    visited = set()

    def _dfs(vertex, parent):
        visited.add(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                if _dfs(neighbor, vertex):
                    return True
            elif neighbor != parent:
                return True  # visited and not parent → cycle!

        return False

    for vertex in graph:
        if vertex not in visited:
            if _dfs(vertex, None):
                return True
    return False


# ── Demo ──
if __name__ == "__main__":
    # Directed graph WITH a cycle (A → B → D → A)
    directed_cyclic = {
        "A": ["B"],
        "B": ["C", "D"],
        "C": [],
        "D": ["A"],
    }
    print("Directed cyclic graph:")
    for v, n in sorted(directed_cyclic.items()):
        print(f"  {v} → {n}")
    print(f"  Has cycle? {has_cycle_directed(directed_cyclic)}\n")

    # Directed graph WITHOUT a cycle (DAG)
    directed_acyclic = {
        "Math": ["Physics", "Stats"],
        "Physics": ["ML"],
        "Stats": ["ML"],
        "ML": ["Deep Learning"],
        "Deep Learning": [],
    }
    print("Directed acyclic graph (DAG):")
    for v, n in sorted(directed_acyclic.items()):
        print(f"  {v} → {n}")
    print(f"  Has cycle? {has_cycle_directed(directed_acyclic)}\n")

    # Undirected graph WITH a cycle (A-B-D-C-A)
    undirected_cyclic = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "D"],
        "D": ["B", "C"],
    }
    print("Undirected cyclic graph:")
    for v, n in sorted(undirected_cyclic.items()):
        print(f"  {v} → {n}")
    print(f"  Has cycle? {has_cycle_undirected(undirected_cyclic)}\n")

    # Undirected TREE (no cycle)
    undirected_tree = {
        "A": ["B", "C"],
        "B": ["A"],
        "C": ["A", "D"],
        "D": ["C"],
    }
    print("Undirected tree (no cycle):")
    for v, n in sorted(undirected_tree.items()):
        print(f"  {v} → {n}")
    print(f"  Has cycle? {has_cycle_undirected(undirected_tree)}")
