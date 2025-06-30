from typing import List

class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.adj_list = {}

        # Build adjacency list from edge list
        for u, v in self.edges:
            if u not in self.adj_list:
                self.adj_list[u] = []
            if v not in self.adj_list:
                self.adj_list[v] = []

            # Avoid duplicate edges
            if v not in self.adj_list[u]:
                self.adj_list[u].append(v)

    def has_cycle(self):
        # Initialize indegrees of all nodes
        indegrees = {u: 0 for u in self.adj_list}

        # Count incoming edges for each node
        for u in self.adj_list:
            for v in self.adj_list[u]:
                indegrees[v] += 1

        # Collect nodes with no incoming edges
        queue = [u for u in indegrees if indegrees[u] == 0]

        topo_sort = []  # To store topological order

        # Kahn's Algorithm for Topological Sorting
        while queue:
            u = queue.pop(0)
            topo_sort.append(u)

            # Decrease indegree of neighbors
            for v in self.adj_list.get(u, []):
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    queue.append(v)

        # If topo_sort doesn't include all nodes, there's a cycle
        return len(self.adj_list) != len(topo_sort)

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = Graph(prerequisites)
        # If the graph has a cycle, can't finish all courses
        return False if graph.has_cycle() else True

# Example usage
numCourses = 2
prerequisites = [[1, 0]]
sol = Solution()
print(sol.canFinish(numCourses, prerequisites))  # Output: True