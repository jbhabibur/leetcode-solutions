from typing import List
from collections import defaultdict

class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.adj_list = defaultdict(set)  # Use a set to avoid duplicate edges

        # Build the adjacency list from the edge list (undirected graph)
        for u, v in self.edges:
            self.adj_list[u].add(v)
            self.adj_list[v].add(u)

    def dfs(self, source, destination):
        visited = set()  # Keep track of visited nodes to avoid cycles

        def dfs_recursively(u, destination):
            if u == destination:
                return True  # Found the destination node
            visited.add(u)  # Mark current node as visited

            for v in self.adj_list.get(u, []):
                if v not in visited:
                    if dfs_recursively(v, destination):
                        return True  # Path found

            return False  # No path found from this route

        return dfs_recursively(source, destination)

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = Graph(edges)  # Build the graph

        return graph.dfs(source, destination)  # Check if path exists

# Example usage
n = 3
edges = [[0, 1], [1, 2], [2, 0]]
source = 0
destination = 2
sol = Solution()
print(sol.validPath(n, edges, source, destination))
