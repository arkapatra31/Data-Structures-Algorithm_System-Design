"""
01 — Graph Class (Adjacency List)
==================================
Foundation class supporting directed/undirected + weighted/unweighted graphs.
"""

from collections import defaultdict


class Graph:
    """Adjacency list graph — directed or undirected, weighted or unweighted."""

    def __init__(self, directed=False):
        self.adj_list = defaultdict(list)  # {vertex: [(neighbor, weight), ...]}
        self.directed = directed

    def add_vertex(self, vertex):
        _ = self.adj_list[vertex]  # accessing the key creates it if missing

    def add_edge(self, v1, v2, weight=1):
        self.adj_list[v1].append((v2, weight))
        if not self.directed:
            self.adj_list[v2].append((v1, weight))

    def remove_edge(self, v1, v2):
        self.adj_list[v1] = [(n, w) for n, w in self.adj_list[v1] if n != v2]
        if not self.directed:
            self.adj_list[v2] = [(n, w) for n, w in self.adj_list[v2] if n != v1]

    def remove_vertex(self, vertex):
        for v in self.adj_list:
            self.adj_list[v] = [(n, w) for n, w in self.adj_list[v] if n != vertex]
        del self.adj_list[vertex]

    def get_neighbors(self, vertex):
        """Return list of neighbor names (without weights)."""
        return [n for n, w in self.adj_list.get(vertex, [])]

    def get_vertices(self):
        return list(self.adj_list.keys())

    def display(self):
        for vertex in sorted(self.adj_list, key=str):
            edges = ", ".join(
                f"{n}(w={w})" if w != 1 else str(n)
                for n, w in self.adj_list[vertex]
            )
            print(f"  {vertex} → [{edges}]")


# ── Demo ──
if __name__ == "__main__":
    g = Graph(directed=False)
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("C", "D")

    print("Graph (undirected):")
    g.display()

    print(f"\nNeighbors of A: {g.get_neighbors('A')}")
    print(f"All vertices:   {g.get_vertices()}")

    g.remove_edge("A", "C")
    print("\nAfter removing edge A-C:")
    g.display()
