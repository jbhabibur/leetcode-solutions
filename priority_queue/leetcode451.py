def heapify_up(heap, i):
    """Restore max-heap property from current node to root"""

    parent = (i - 1) // 2
    while parent >= 0 and heap[parent][1]["fq"] < heap[i][1]["fq"]:
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

    # If left child exists and greater than current largest
    if left < n and heap[largest][1]["fq"] < heap[left][1]["fq"]:
        largest = left

    # If right child exists and greater than current largest
    if right < n and heap[largest][1]["fq"] < heap[right][1]["fq"]:
        largest = right

    if largest != i:
        heap[largest], heap[i] = heap[i], heap[largest]
        heapify_down(heap, largest)

def enqueue(heap: list[tuple[str, int]], item, priority):
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

    # Replace root with last node and remove last node
    heap[0] = heap.pop()

    heapify_down(heap, 0)

    return max_item

class Solution:
    def __init__(self):
        self.heap = []

    def frequencySort(self, s: str) -> str:
        hash_map = dict() # Dictionary to count frequency and store repeated characters

        for char in s:
            if char not in hash_map: # First appearance
                hash_map[char] = {"fq": 1, "path": char}
            else:
                hash_map[char]["fq"] = hash_map[char]["fq"] + 1 # Increment frequency
                hash_map[char]["path"] = hash_map[char]["path"] + char # Append character

        # Push each character into the priority queue using its frequency as priority
        for char, frequency in hash_map.items():
            enqueue(self.heap, char, frequency)

        # Extract characters in order of highest frequency to lowest
        result = []
        for _ in hash_map:
            char, frequency = dequeue(self.heap)
            result.append(frequency["path"])

        return "".join(result)

# Example usage
solution = Solution()

s = "Aabb"
print(solution.frequencySort(s))


