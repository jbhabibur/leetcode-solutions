from typing import List
from collections import deque  # For efficient BFS queue

class Graph:
    def __init__(self, grid):
        self.grid = grid  # The binary grid: 1 = land, 0 = water
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.adj_list = {}  # Adjacency list representation of the graph

        self.build_graph()  # Automatically build graph on initialization

    def is_valid(self, row, col):
        # Check if the cell is within bounds and is land
        return 0 <= row < self.rows and 0 <= col < self.cols and self.grid[row][col] == 1

    def build_graph(self):
        # Define the 4 directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] == 1:
                    self.adj_list[(row, col)] = []

                    for dr, dc in directions:
                        new_row = row + dr
                        new_col = col + dc

                        if self.is_valid(new_row, new_col):
                            self.adj_list[(row, col)].append((new_row, new_col))

                            # Optional: add reverse edge to simulate undirected graph
                            if (new_row, new_col) not in self.adj_list:
                                self.adj_list[(new_row, new_col)] = []

                            if (row, col) not in self.adj_list[(new_row, new_col)]:
                                self.adj_list[(new_row, new_col)].append((row, col))

    def all_connected_components(self):
        max_area = 0
        visited = set()

        for node in self.adj_list:
            if node not in visited:
                area = 0
                visited.add(node)
                queue = deque([node])  # Use deque for efficient popping

                while queue:
                    u = queue.popleft()
                    area += 1

                    for neighbor in self.adj_list[u]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)

                max_area = max(max_area, area)

        return max_area

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        g = Graph(grid)
        return g.all_connected_components()

# Example usage
grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
]

sol = Solution()
print(sol.maxAreaOfIsland(grid))  # Expected output: 6
