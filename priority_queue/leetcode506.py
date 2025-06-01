from typing import List

def heapify_up(heap, i):
    """Restore max-heap property from current not to root"""

    parent = (i - 1) // 2
    while parent >= 0 and heap[parent][0] < heap[i][0]:
        heap[parent], heap[i] = heap[i], heap[parent]

        # Update current node and its parent
        i = parent
        parent = (i - 1) // 2

def heapify_down(heap, i):
    """Restore max-heap property from current node to its subtree"""

    largest = i
    left = (2 * i) + 1
    right = (2 * i) + 2

    n = len(heap)

    # If left child exits and greater than current largest
    if left < n and heap[largest][0] < heap[left][0]:
        largest = left

    # If right child exits and greater than current largest
    if right < n and heap[largest][0] < heap[right][0]:
        largest = right

    if largest !=  i:
        heap[largest], heap[i] = heap[i], heap[largest]
        heapify_down(heap, largest)

def enqueue(heap, item, priority):
    """Push an item in the priority queue"""

    heap.append((item, priority))
    heapify_up(heap, len(heap) - 1)

def dequeue(heap):
    """Return and remove root item (maximum in max-heap)"""

    if not heap:
        return None

    if len(heap) == 1:
        return heap.pop()

    # Store root item (maximum in max-heap) to return later
    max_item = heap[0]

    # Replace root item (maximum in max-heap) with last node and remove last node
    heap[0] = heap.pop()

    heapify_down(heap, 0)

    return max_item

class Solution:
    def __init__(self):
        self.heap = []

    def findRelativeRanks(self, score: List[int]) -> List[str]:
        for i in range(len(score)):
            enqueue(self.heap, score[i], i)

        answer = [""] * len(score)

        for i in range(len(score)):
            (position, index) = dequeue(self.heap)
            if i == 0:
                answer[index] = "Gold Medal"
            elif i == 1:
                answer[index] = "Silver Medal"
            elif i == 2:
                answer[index] = "Bronze Medal"
            else:
                answer[index] = f"{i + 1}"

        return answer

# Example usage
solution = Solution()

score = [5,4,3,2,1]
print(solution.findRelativeRanks(score))

