from typing import List

class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.adj_list = {}

        # Build adjacency list from input graph
        for u, v in enumerate(self.graph):
            self.adj_list[u] = v

    def find_all_path(self, target):
        result = []   # Stores all valid paths from source to target
        current = []  # Temporarily holds the current path

        # Backtracking helper function
        def backtrack(u, target):
            current.append(u)  # Add current node to the path

            if u == target:  # If target is reached, add path to result
                result.append(current[:])
                return

            # Explore all neighbors
            for v in self.adj_list[u]:
                backtrack(v, target)
                current.pop()  # Backtrack: remove last node to explore new paths

        backtrack(0, target)  # Start from source node (0)
        return result

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        g = Graph(graph)
        n = len(graph)
        return g.find_all_path(n - 1)  # Find paths from 0 to n-1

# Example usage
sol = Solution()
graph = [[4,3,1],[3,2,4],[],[4],[]]
print(sol.allPathsSourceTarget(graph))