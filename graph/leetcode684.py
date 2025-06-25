from typing import List

class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.adj_list = {}  # Initialize an empty adjacency list

    def detect_cycle_on_build(self):
        # Try adding each edge one by one and check for a cycle
        for u, v in self.edges:
            self.build_graph(u, v)         # Add edge to the graph
            result = self.has_cycle()      # Check for cycle after adding

            if result:                     # If cycle found, this edge is redundant
                return [u, v]

    def build_graph(self, u, v):
        # Add nodes to adjacency list if not present
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []

        # Add the edge both ways since the graph is undirected
        if v not in self.adj_list[u]:
            self.adj_list[u].append(v)
        if u not in self.adj_list[v]:
            self.adj_list[v].append(u)

    def has_cycle(self):
        visited = set()  # Keep track of visited nodes

        # Try BFS from each unvisited node
        for u in self.adj_list:
            if u not in visited:
                visited.add(u)
                queue = [(u, None)]  # Queue stores (current_node, parent)

                while queue:
                    u, parent = queue.pop(0)

                    for v in self.adj_list.get(u, []):
                        if v not in visited:
                            visited.add(v)
                            queue.append((v, u))
                        elif v != parent:
                            # Found a back edge to a previously visited node that is not the parent
                            return True  # Cycle detected
        return False  # No cycle found

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = Graph(edges)
        return graph.detect_cycle_on_build()  # Return the redundant edge that caused the cycle

# Example usage
edges = [[1,2],[1,3],[2,3]]
sol = Solution()
print(sol.findRedundantConnection(edges))  # Output: [2, 3]
