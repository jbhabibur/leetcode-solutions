from typing import List

class Graph:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])
        self.adj_list = {}  # Adjacency list to represent graph
        self.build_graph()

    def build_graph(self):
        # Build an undirected graph from the isConnected matrix
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] == 1:
                    # Ensure both nodes are in the adjacency list
                    if row not in self.adj_list:
                        self.adj_list[row] = []
                    if col not in self.adj_list:
                        self.adj_list[col] = []

                    # Add bidirectional edges if not self-loop
                    if row != col:
                        if col not in self.adj_list[row]:
                            self.adj_list[row].append(col)
                        if row not in self.adj_list[col]:
                            self.adj_list[col].append(row)

    def all_connected_components(self):
        count = 0  # Count of connected components
        visited = set()

        for u in self.adj_list:
            if u not in visited:
                # Start DFS from unvisited node
                stack = [u]
                while stack:
                    u = stack.pop()
                    visited.add(u)
                    for v in self.adj_list.get(u, []):
                        if v not in visited:
                            visited.add(v)
                            stack.append(v)
                count += 1  # One full component visited

        return count

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = Graph(isConnected)
        return graph.all_connected_components()  # Return number of provinces

# Example usage
isConnected = [[1,0,0],[0,1,0],[0,0,1]]
sol = Solution()
print(sol.findCircleNum(isConnected))  # Output: 3
