# Problem :https://leetcode.com/problems/clone-graph/?envType=problem-list-v2&envId=oizxjoit
# problem statement in simple words:
# Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.
# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
# The test cases are generated in the following format (graph serialization):
# Nodes are labeled from 1 to N.
# The given node will always be the first node with val = 1.
# You must return the copy of the given node as a reference to the cloned graph.

from typing import Optional


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # if not node:
        #     return None

        # old_to_new = {}

        # def dfs(node):
        #     if node in old_to_new:
        #         return old_to_new[node]

        #     copy = Node(node.val)
        #     old_to_new[node] = copy

        #     for neighbor in node.neighbors:
        #         copy.neighbors.append(dfs(neighbor))

        #     return copy

        # return dfs(node)
        if not node:
            return None
        map = {}
        def dfs(node):
            if node.val in map:
                return map[node.val]
            copy = Node(node.val)
            map[node.val] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        return dfs(node)
    
if __name__ == "__main__":
    # Create a sample graph
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]

    # input = [[2,4],[1,3],[2,4],[1,3]]
    # output = [[2,4],[1,3],[2,4],[1,3]]

    solution = Solution()
    cloned_graph = solution.cloneGraph(node1)
    print(cloned_graph.val)  # Should print 1
    print([neighbor.val for neighbor in cloned_graph.neighbors])  # Should print [2, 4]


# Strategy to solve the problem:
# 1. Use Depth-First Search (DFS) to traverse the graph and create a copy of each node.
# 2. Maintain a mapping (dictionary) from original nodes to their
#    corresponding cloned nodes to avoid infinite loops and ensure that each node is cloned only once.
# 3. For each node, recursively clone its neighbors and add them to the neighbors list of the cloned node.
# 4. Return the cloned node corresponding to the input node as the entry point to the cloned graph.