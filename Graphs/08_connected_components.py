"""
08 — Connected Components
===========================
Finds all groups of vertices that can reach each other in an undirected graph.
Each component is an "island" — every vertex within it is reachable from every other.
Time: O(V + E)  |  Space: O(V)
"""


def connected_components(graph):
    """
    Find all connected components using DFS.

    Args:
        graph: dict — {vertex: [neighbors]}  (undirected)

    Returns:
        list of sets — each set is one connected component
    """
    visited = set()
    components = []

    for vertex in graph:
        if vertex not in visited:
            # Start a new component
            component = set()
            stack = [vertex]

            while stack:
                v = stack.pop()
                if v not in visited:
                    visited.add(v)
                    component.add(v)
                    for neighbor in graph[v]:
                        if neighbor not in visited:
                            stack.append(neighbor)

            components.append(component)

    return components


def is_connected(graph):
    """Check if the entire graph is connected (single component)."""
    return len(connected_components(graph)) == 1


def largest_component(graph):
    """Return the largest connected component."""
    components = connected_components(graph)
    return max(components, key=len) if components else set()


# ── Demo ──
if __name__ == "__main__":
    # Graph with 3 separate components
    graph = {
        # Component 1: social group
        "Alice":  ["Bob", "Carol"],
        "Bob":    ["Alice", "Carol"],
        "Carol":  ["Alice", "Bob"],

        # Component 2: isolated pair
        "Dave":   ["Eve"],
        "Eve":    ["Dave"],

        # Component 3: lone node
        "Frank":  [],
    }

    print("Social network graph:")
    for v, neighbors in sorted(graph.items()):
        print(f"  {v} → {neighbors if neighbors else '(isolated)'}")

    components = connected_components(graph)
    print(f"\nNumber of components: {len(components)}")
    for i, comp in enumerate(components, 1):
        print(f"  Component {i}: {sorted(comp)}")

    print(f"\nIs fully connected? {is_connected(graph)}")
    print(f"Largest component:  {sorted(largest_component(graph))}")

    # Now connect everyone
    print("\n--- After connecting Dave to Alice ---")
    graph["Dave"].append("Alice")
    graph["Alice"].append("Dave")
    graph["Frank"].append("Eve")
    graph["Eve"].append("Frank")

    components2 = connected_components(graph)
    print(f"Number of components: {len(components2)}")
    for i, comp in enumerate(components2, 1):
        print(f"  Component {i}: {sorted(comp)}")
    print(f"Is fully connected? {is_connected(graph)}")
