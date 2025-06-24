from typing import List

class Graph:
    def __init__(self, rooms):
        self.rooms = rooms
        self.adj_list = {}

        # Build the adjacency list: each room points to its list of keys (i.e., connected rooms)
        for i, v in enumerate(self.rooms):
            self.adj_list[i] = v

    def bfs(self):
        result = []

        # Start BFS from room 0 (assumed to always be unlocked)
        start = next(iter(self.adj_list))  # which is 0
        visited = {start}
        queue = [start]

        while queue:
            u = queue.pop(0)      # Dequeue current room
            result.append(u)      # Mark it as visited (in result)

            # Check all keys (connected rooms) in the current room
            for v in self.adj_list.get(u, []):
                if v not in visited:
                    visited.add(v)     # Mark as visited
                    queue.append(v)    # Enqueue the connected room

        return result  # List of all visited rooms

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = Graph(rooms)
        # If BFS visits all rooms, return True
        return len(graph.bfs()) == len(rooms)

rooms = [[]]
sol = Solution()
print(sol.canVisitAllRooms(rooms))  # Output: True (because room 0 is already open)
