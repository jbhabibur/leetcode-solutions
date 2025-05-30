from typing import List

class Solution:
    def __init__(self):
        self.heap = [] # Array to represent complete binary tree

    def _heapify_up(self, i):
        """Helper function to restore max-heap property from current node to root"""

        parent = (i - 1) // 2
        while parent >= 0 and self.heap[parent] < self.heap[i]:
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]

            # Update current node and its parent node
            i = parent
            parent = (i - 1) // 2

    def _heapify_down(self, i):
        """Helper function to restore max-heap property from current node to it's subtree"""

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
            # Restore the max-heap property
            self._heapify_down(largest)

    def enqueue(self, item):
        """Enqueue an item to the priority queue and restore the max-heap property"""

        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def dequeue(self):
        """Remove and return the root element with the highest priority value from the priority queue"""
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        # Store the root item (maximum in max-heap) to return later
        max_item = self.heap[0]

        # Replace root item with last node and remove last node
        last_node = self.heap.pop()
        self.heap[0] = last_node

        # Restore the max-heap property
        self._heapify_down(0)

        return max_item

    def maxProduct(self, nums: List[int]) -> int:
        # Enqueue items to to priority queue
        for num in nums:
            self.enqueue(num)

        # Heap sort
        sorted_arr = []
        while self.heap:
            sorted_arr.append(self.dequeue())

        return (sorted_arr[0] - 1) * (sorted_arr[1] - 1)

# Example usage
solution = Solution()

nums = [3,7]
print(solution.maxProduct(nums))