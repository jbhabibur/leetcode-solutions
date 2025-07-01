from typing import List

class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges

        # Initialize adjacency list
        self.adj_list = {u: [] for u in range(self.nodes)}

        # Build graph with reversed edges (v -> u)
        for u, v in self.edges:
            if v in self.adj_list:
                self.adj_list[v].append(u)

    def topological_sort(self):
        # Compute indegrees of all nodes
        indegrees = {u: 0 for u in self.adj_list}
        for u in self.adj_list:
            for v in self.adj_list[u]:
                indegrees[v] += 1

        # Start with nodes having zero indegree
        queue = [u for u in self.adj_list if indegrees[u] == 0]
        topo_sort = []

        # Kahn's algorithm for topological sort
        while queue:
            u = queue.pop(0)
            topo_sort.append(u)

            for v in self.adj_list.get(u, []):
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    queue.append(v)

        # Return empty list if cycle detected
        return topo_sort if len(topo_sort) == len(self.adj_list) else []

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = Graph(numCourses, prerequisites)

        return graph.topological_sort()

# Example usage
numCourses = 3
prerequisites = [[1,0],[1,2],[0,1]]
sol = Solution()
print(sol.findOrder(numCourses, prerequisites))
