from typing import List

class Graph:
    def __init__(self, grid):
        self.grid = grid  # The 2D grid of '1's (land) and '0's (water)
        self.rows = len(grid)  # Number of rows in the grid
        self.cols = len(grid[0])  # Number of columns in the grid
        self.adj_list = {}  # Adjacency list to represent graph connections

        self.build_graph()  # Build the graph based on the grid

    # Check if a cell is within bounds and is land ("1")
    def is_valid(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols and self.grid[row][col] == "1"

    # Build the graph from the grid
    def build_graph(self):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 4-directional movement: up, down, left, right

        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] == "1":  # Only consider land cells
                    self.adj_list[(row, col)] = []  # Initialize adjacency list for the cell

                    for delta_row, delta_col in directions:
                        new_row = row + delta_row
                        new_col = col + delta_col

                        # If the neighboring cell is valid land
                        if self.is_valid(new_row, new_col):
                            self.adj_list[(row, col)].append((new_row, new_col))  # Add neighbor

                            # Ensure the neighbor also has an entry in adj_list
                            if (new_row, new_col) not in self.adj_list:
                                self.adj_list[(new_row, new_col)] = []

                            # Add the current cell as neighbor (making the edge undirected)
                            if (row, col) not in self.adj_list[(new_row, new_col)]:
                                self.adj_list[(new_row, new_col)].append((row, col))

    # Find the number of connected components (islands) using BFS
    def all_connected_components(self):
        island = 0  # Count of islands
        visited = set()  # Track visited nodes

        for node in self.adj_list:
            if node not in visited:
                island += 1  # Start of a new island
                visited.add(node)
                queue = [node]  # BFS queue

                while queue:
                    u = queue.pop(0)  # Dequeue

                    for v in self.adj_list[u]:  # Explore all neighbors
                        if v not in visited:
                            visited.add(v)
                            queue.append(v)  # Enqueue unvisited neighbor

        return island  # Total number of islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        g = Graph(grid)  # Build graph from grid
        return g.all_connected_components()  # Count and return number of islands

# Example usage
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

sol = Solution()
print(sol.numIslands(grid))  # Output: 3
