from typing import List

def heapify_up(heap, i):
    """Restore max-heap by heapify up from current node to root"""

    parent = (i - 1) // 2
    # Restore max-heap by heapify up from current node to root
    while parent >= 0 and heap[parent] < heap[i]:
        heap[parent], heap[i] = heap[i], heap[parent]

        # Update current node and its parent
        i = parent
        parent = (i - 1) // 2

def heapify_down(heap, i):
    """Restore max-heap from current node to its subtree"""

    largest = i
    left = (2 * i) + 1
    right = (2 * i) + 2

    n = len(heap)

    # If left child exists and greater than current largest
    if left < n and heap[largest] < heap[left]:
        largest = left

    # If right child exists and greater than current largest
    if right < n and heap[largest] < heap[right]:
        largest = right

    if largest != i:
        heap[largest], heap[i] = heap[i], heap[largest]
        heapify_down(heap, largest)

def enqueue(heap, val):
    """Push an item into priority queue"""

    heap.append(val) # Push item into priority queue
    heapify_up(heap, len(heap) - 1) # Restore max-heap property

def dequeue(heap):
    """Return and remove root item (maximum in max-heap) from the prority queue"""

    if not heap:
        return None

    if len(heap) == 1:
        return heap.pop() # Return root item and remove it

    # Store root item (maximum in max-heap) to return later
    max_item = heap[0]

    # Replace root item with last node
    heap[0] = heap.pop()

    # Restore max-heap property
    heapify_down(heap, 0)

    return max_item

class Solution:
    def __init__(self):
        self.heap = []

    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Push items into priority queue
        for num in nums:
            enqueue(self.heap, num)

        # Extract kth largest item
        max_item = None
        for _ in range(k):
            max_item = dequeue(self.heap)
        return max_item

# Example usage
solution = Solution()

nums = [3,2,1,5,6,4]
k = 2
print(solution.findKthLargest(nums, k))

