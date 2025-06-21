from typing import List

class Graph:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.adj_list = {}
        self.build_graph()  # Create graph from grid

    def is_valid(self, row, col):
        # Check if cell is within bounds and is land (1)
        return 0 <= row < self.rows and 0 <= col < self.cols and self.grid[row][col] == 1

    def build_graph(self):
        # Directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] == 1:
                    self.adj_list[(row, col)] = []

                    for dr, dc in directions:
                        new_row, new_col = row + dr, col + dc

                        if self.is_valid(new_row, new_col):
                            self.adj_list[(row, col)].append((new_row, new_col))

                            # Initialize neighbor's list if not present
                            if (new_row, new_col) not in self.adj_list:
                                self.adj_list[(new_row, new_col)] = []

                            # Make the edge bidirectional
                            if (row, col) not in self.adj_list[(new_row, new_col)]:
                                self.adj_list[(new_row, new_col)].append((row, col))

    def all_connected_components(self):
        # Return all connected components using BFS
        components = []
        visited = set()

        for node in self.adj_list:
            if node not in visited:
                component = []
                queue = [node]
                visited.add(node)

                while queue:
                    u = queue.pop(0)
                    component.append(u)

                    for v in self.adj_list[u]:
                        if v not in visited:
                            visited.add(v)
                            queue.append(v)

                components.append(component)

        return components

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        g = Graph(grid)
        count = 0
        components = g.all_connected_components()

        for component in components:
            enclaves = True

            # If any cell in the component touches border, it's not an enclave
            for u, v in component:
                if u == 0 or v == 0 or u == len(grid) - 1 or v == len(grid[0]) - 1:
                    enclaves = False

            if enclaves:
                count += len(component)  # Count enclave land cells

        return count

# Example usage
grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
sol = Solution()
print(sol.numEnclaves(grid))  # Output: 3
