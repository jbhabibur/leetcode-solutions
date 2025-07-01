from typing import List

class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.adj_list = {}

        # Build adjacency list representation from input graph list
        for i, neighbors in enumerate(self.graph):
            self.adj_list[i] = neighbors

    def dfs_check(self, u, visited, path_visited, check):
        visited[u] = True
        path_visited[u] = True  # Mark node as in current DFS path

        for v in self.adj_list.get(u, []):
            if not visited.get(v, False):
                # If neighbor not visited, recurse
                if self.dfs_check(v, visited, path_visited, check):
                    return True  # Cycle detected deeper in recursion
            elif path_visited.get(v, False):
                # If neighbor is in current DFS path, cycle found
                return True

        # Backtrack: current node is removed from current DFS path
        path_visited[u] = False
        # Mark node as safe since no cycle was found starting from it
        check[u] = True
        return False  # No cycle detected from this node

    def find_safe_nodes(self):
        visited, path_visited, check = {}, {}, {}
        for u in self.adj_list:
            if not visited.get(u, False):
                self.dfs_check(u, visited, path_visited, check)

        # Collect all nodes marked safe
        return sorted([node for node, safe in check.items() if safe])

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        graph_obj = Graph(graph)
        return graph_obj.find_safe_nodes()

# Example usage
graph = [[1, 2], [2, 3], [5], [0], [5], [], []]
sol = Solution()
print(sol.eventualSafeNodes(graph))  # Output: [2, 4, 5, 6]