from typing import List

class Solution:
    def __init__(self):
        self.heap = [] # Array to represent complete binary tree

    def _heapify_up(self, i):
        """Helper function to restore min-heap property from current node to root"""

        parent = (i - 1) // 2
        while parent >= 0 and self.heap[parent] > self.heap[i]:
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]

            # Update the current node and it's parent node
            i = parent
            parent = (i - 1) // 2

    def _heapify_down(self, i):
        """Helper function to restore min-heap property from current node to it's subtree"""

        smallest = i
        left = (2 * i) + 1
        right = (2 * i) + 2

        n = len(self.heap)

        # Check if left child exists and is less than current smallest
        if left < n and self.heap[smallest] > self.heap[left]:
            smallest = left

        # Check if right child exists and is less than current smallest
        if right < n and self.heap[smallest] > self.heap[right]:
            smallest = right

        if smallest != i:
            self.heap[smallest], self.heap[i] = self.heap[i], self.heap[smallest]

            # Restore min-heap property from current node to it's subtree
            self._heapify_down(smallest)

    def _extract_min(self):
        """Return and remove the root item (minimum in min-heap) from the heap"""

        if len(self.heap) == 1:
            return self.heap.pop()

        # Store the root node (minimum in min-heap) to return later
        min_item = self.heap[0]

        # Replace the root node with the last node and remove the last node
        last_node = self.heap.pop()
        self.heap[0] = last_node

        # Restore the min-heap property
        self._heapify_down(0)

        return min_item

    def enqueue(self, item):
        """Enqueue an item to the priority queue and restore the min-heap property"""

        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def dequeue(self):
        """Remove and return the root item with the lowest priority value from the priority queue"""

        min_item = self._extract_min()
        return min_item

    def numberGame(self, nums: List[int]) -> List[int]:
        # Enqueued items to the priority queue
        for num in nums:
            self.enqueue(num)

        sorted_arr = []
        # Sorting in ascending order by heap sort
        while self.heap:
            sorted_arr.append(self._extract_min())

        for i in range(0, len(sorted_arr), 2):
            sorted_arr[i - 2], sorted_arr[i - 1] = sorted_arr[i - 1], sorted_arr[i - 2]

        return sorted_arr

# Example usage
solution = Solution()

nums = [2, 5]
print(solution.numberGame(nums))