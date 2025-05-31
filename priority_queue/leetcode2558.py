from typing import List
import math

class Solution:
    def __init__(self):
        self.heap = [] # Array to represent complete binary tree

    def _heapify_up(self, i):
        """Helper function to restore max-heap property from current node to root"""

        parent = (i - 1) // 2
        while parent >= 0 and self.heap[parent] < self.heap[i]:
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]

            # Update current node and its parent
            i = parent
            parent = (i - 1) // 2

    def _heapify_down(self, i):
        """Helper function to restore max-heap property from current node to its subtree"""

        largest = i
        left = (2 * i) + 1
        right = (2 * i) + 2

        n = len(self.heap)

        # Check if left child exists and greater than current largest
        if left < n and self.heap[largest] < self.heap[left]:
            largest = left

        # Check if right child exists and greater than current largest
        if right < n and self.heap[largest] < self.heap[right]:
            largest = right

        if largest != i:
            self.heap[largest], self.heap[i] = self.heap[i], self.heap[largest]
            self._heapify_down(largest)

    def _extract_max(self):
        """Return and remove the root item (maximum in max-heap) from the heap"""

        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        # Store the root item (maximum in max-heap) to return later
        max_item = self.heap[0]

        # Replace root item with last node and remove last node
        self.heap[0] = self.heap.pop()

        # Restore max-heap property
        self._heapify_down(0)

        return max_item

    def enqueue(self, val):
        """Push item at the end of the priority queue"""

        self.heap.append(val) # Push item at the end of the priority queue
        self._heapify_up(len(self.heap) - 1) # Restore max-heap property

    def dequeue(self):
        """Return and remove the root item with the highest priority value from the priority queue"""

        return self._extract_max()

    def pickGifts(self, gifts: List[int], k: int) -> int:
        for pile in gifts:
            self.enqueue(pile)

        for i in range(k):
            # Every iteration, extract the maximum gift value, take square root, and reinsert
            max_item = self.dequeue()
            self.enqueue(int(math.sqrt(max_item)))

        return sum(self.heap)

# Example usage
solution = Solution()

gifts = [25,64,9,4,100]
k = 4
print(solution.pickGifts(gifts, k))