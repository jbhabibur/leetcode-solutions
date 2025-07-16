from typing import Optional
from collections import deque

# Define a binary tree node
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# Build binary tree from level-order traversal
def build_binary_tree(values):
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        current = queue.popleft()

        # Process left child
        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1

        # Process right child
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    return root

def bfs(current):
    result = []
    queue = deque([current])  # Initialize queue with root node

    while queue:
        level_size = len(queue)  # Number of nodes at current level
        level = []  # To store values of the current level

        for _ in range(level_size):
            current = queue.popleft()  # Pop the front node in the queue
            level.append(current.val)  # Add its value to the current level

            # Add child nodes of current node to the queue (if they exist)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        result.append(level)  # Add the current level to the result

    return sum(result[-1])  # Return the sum of the last (deepest) level

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        return bfs(root)

# Example usage
root = [6,7,8,2,7,1,3,9,None,1,4,None,None,None,5]
root = build_binary_tree(root)

sol = Solution()
print(sol.deepestLeavesSum(root))