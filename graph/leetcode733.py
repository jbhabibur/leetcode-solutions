from typing import List

class Graph:
    def __init__(self, grid, sr, sc):
        self.grid = grid
        self.rows = len(grid)
        self.initial_color = self.grid[sr][sc]  # Store the starting color
        self.cols = len(grid[0])
        self.adj_list = {}  # Initialize adjacency list

        self.build_graph()  # Build graph based on 4-directional connectivity

    def is_valid(self, row, col):
        # Check if the cell is within bounds and has the same color as the starting cell
        return 0 <= row < self.rows and 0 <= col < self.cols and self.grid[row][col] == self.initial_color

    def build_graph(self):
        # Directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == self.initial_color:
                    self.adj_list[(r, c)] = []  # Create entry for current cell

                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc

                        if self.is_valid(nr, nc):
                            self.adj_list[(r, c)].append((nr, nc))  # Add valid neighbor

                            if (nr, nc) not in self.adj_list:
                                self.adj_list[(nr, nc)] = []

                            if (r, c) not in self.adj_list[(nr, nc)]:
                                self.adj_list[(nr, nc)].append((r, c))  # Make it bidirectional

    def dfs(self, sr, sc, color):
        visited = set()

        def dfs_recursively(u):
            visited.add(u)  # Mark as visited
            row, col = u
            self.grid[row][col] = color  # Change color

            for v in self.adj_list.get(u, []):  # Visit all neighbors
                if v not in visited:
                    dfs_recursively(v)

        dfs_recursively((sr, sc))  # Start DFS from source

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        graph = Graph(image, sr, sc)  # Create graph from image
        graph.dfs(sr, sc, color)  # Perform DFS to change colors

        return graph.grid  # Return the modified image

# Example usage
image = [[0,0,0],[0,0,0]]
sr = 1
sc = 0
color = 2
sol = Solution()
print(sol.floodFill(image, sr, sc, color))  # Output: [[2, 2, 2], [2, 2, 2]]
