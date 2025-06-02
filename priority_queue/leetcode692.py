from typing import List

def heapify_up(heap, i):
    """Restore max-heap by heapify up from current node to root"""

    parent = (i - 1) // 2

    # Restore max-heap by heapify up from current node to root
    # Conditions: More frequent words first. If frequencies are the same, lexicographically `smaller` words first
    while parent >= 0 and (heap[parent][0] < heap[i][0] or
                           (heap[parent][0] == heap[i][0] and heap[parent][1] > heap[i][1])):
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

    # Conditions: More frequent words first. If frequencies are the same, lexicographically `smaller` words first
    if left < n and (heap[largest][0] < heap[left][0] or
                     (heap[largest][0] == heap[left][0] and heap[largest][1] > heap[left][1])):
        largest = left

    if right < n and ((heap[largest][0] < heap[right][0]) or
                     (heap[largest][0] == heap[right][0] and heap[largest][1] > heap[right][1])):
        largest = right

    if largest != i:
        heap[largest], heap[i] = heap[i], heap[largest]
        heapify_down(heap, largest)

def enqueue(heap, word, frequency):
    """Push an item into priority queue"""

    heap.append((frequency, word)) # Push item into priority queue
    heapify_up(heap, len(heap) - 1) # Restore max-heap property

def dequeue(heap):
    """Return and remove root item (maximum in max-heap) from the priority queue"""

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

    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        # Dictionary to count words frequency
        hash_map = dict()

        # Counting frequency using hash map (dictionary)
        for word in words:
            if word not in hash_map:
                hash_map[word] = 1
            else:
                hash_map[word] += 1

        # Build priority queue (using max-heap) to find maximum frequency
        for word, frequency in hash_map.items():
            enqueue(self.heap, word, frequency)

        result = []
        for _ in range(k):
            (frequency, word) = dequeue(self.heap)
            result.append(word)

        return result

# Example usage
solution = Solution()

words = ["i","love","leetcode","i","love","coding"]
k = 3
print(solution.topKFrequent(words, k))