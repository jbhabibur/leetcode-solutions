from typing import List
from collections import defaultdict
import heapq

class Graph:
    def __init__(self, edges, n):
        self.edges = edges
        self.adj_list = defaultdict(list)

        # Ensure all nodes from 1 to n are included
        for u in range(1, n + 1):
            self.adj_list[u] = []

        # Fill adjacency list with directed edges and weights
        for u, v, w in self.edges:
            self.adj_list[u].append((v, w))

    def dijkstra(self, source):
        # Initialize all distances to infinity
        distances = {u: float("inf") for u in self.adj_list}
        distances[source] = 0

        # Min-heap to always expand the node with the smallest distance
        min_heap = [(0, source)]
        while min_heap:
            curr_dist, u = heapq.heappop(min_heap)

            # Ignore outdated entry in heap (a better path to this node already exists)
            if curr_dist > distances[u]:
                continue

            for v, weight in self.adj_list.get(u, []):
                if curr_dist + weight < distances[v]:
                    distances[v] = curr_dist + weight
                    heapq.heappush(min_heap, (distances[v], v))

        # Maximum time taken to reach any node from the source
        max_val = max(distances.values())

        # If any node is unreachable, return -1
        return max_val if max_val != float("inf") else -1

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = Graph(times, n)

        return graph.dijkstra(k)

# Example usage
times = [[1,2,1]]
n = 2
k = 2
sol = Solution()
print(sol.networkDelayTime(times, n, k))