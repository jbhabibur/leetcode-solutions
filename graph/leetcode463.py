from typing import List

class Graph:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.adj_list = {}  # Graph represented as an adjacency list

        self.build_graph()

    def is_valid(self, row, col):
        # Check if cell is within bounds and is land (1)
        return 0 <= row < self.rows and 0 <= col < self.cols and self.grid[row][col] == 1

    def build_graph(self):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 4-connected directions

        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] == 1:
                    self.adj_list[(row, col)] = []

                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc
                        if self.is_valid(nr, nc):
                            # Connect current land cell with adjacent land cell
                            self.adj_list[(row, col)].append((nr, nc))
                            # Ensure undirected connection
                            if (nr, nc) not in self.adj_list:
                                self.adj_list[(nr, nc)] = []
                            if (row, col) not in self.adj_list[(nr, nc)]:
                                self.adj_list[(nr, nc)].append((row, col))

    def is_valid_perimeter(self, row, col):
        # Return True if water or out of bounds (counts as perimeter)
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.grid[row][col] == 0
        return True

    def bfs(self):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        count = 0

        start = next(iter(self.adj_list))  # Start from any land cell
        visited = {start}
        queue = [start]

        while queue:
            r, c = queue.pop(0)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if self.is_valid_perimeter(nr, nc):
                    count += 1  # Count sides touching water or boundary

            for neighbor in self.adj_list[(r, c)]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return count

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        graph = Graph(grid)
        return graph.bfs()

# Example usage
grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
sol = Solution()
print(sol.islandPerimeter(grid))  # Output: 16