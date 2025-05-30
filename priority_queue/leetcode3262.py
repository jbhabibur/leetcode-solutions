from typing import List

class Solution:
    def __init__(self):
        self.heap = [] # Array to represent a complete binary tree

    def _heapify_up(self, i):
        """Helper function to restore min-heap property from current node to root"""

        parent = (i - 1) // 2
        while parent >= 0 and self.heap[parent] > self.heap[i]: # Comparing lexicographical order
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]

            # Update the index of the current node and it's parent node
            i = parent
            parent = (i - 1) // 2

    def _heapify_down(self, i):
        """Helper function to restore min-heap property from current node to it's subtree"""

        smallest = i
        left = (2 * i) + 1
        right = (2 * i) + 2

        n = len(self.heap)

        if left < n and self.heap[smallest] > self.heap[left]: # Comparing lexicographical order
            smallest = left

        if right < n and self.heap[smallest] > self.heap[right]: # Comparing lexicographical order
            smallest = right

        if smallest != i:
            self.heap[smallest], self.heap[i] = self.heap[i], self.heap[smallest]
            self._heapify_down(smallest)

    def _extract_min(self):
        """Helper function to return and remove the root item (minimum in min-heap) from the heap"""

        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        # Store the root item (minimum in min-heap) to return it later
        min_item = self.heap[0]

        # Replace the root node with the last node and remove the last node
        last_item = self.heap.pop()
        self.heap[0] = last_item

        # Restore the min-heap property after deleting the root item everytime
        self._heapify_down(0)

        return min_item

    def enqueue(self, priority, index):
        """Push an item to the priority queue and restore the min-heap property based on its priority"""

        self.heap.append((priority, index)) # Push an item in the queue

        self._heapify_up(len(self.heap) - 1) # Restore the min-heap property

    def dequeue(self):
        """Remove and return the item with the lowest priority value from the priority queue"""

        return self._extract_min()

    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        # Enqueued items and restore min-heap property
        for i in range(len(nums)):
            self.enqueue(nums[i], i)

        # Dequeued min item and multiply
        for _ in range(k):
            (priority, i) = self.dequeue()
            self.enqueue(priority * multiplier, i)

        # Sorting list of tuples based on their second value
        self.heap = sorted(self.heap, key=lambda x: x[1])

        return [val for val, _ in self.heap]

# Example usage
solution = Solution()

nums = [5,5,1,2,5,2,1,3,3,2,1,5]
k = 5
multiplier = 2
print(solution.getFinalState(nums, k, multiplier))
