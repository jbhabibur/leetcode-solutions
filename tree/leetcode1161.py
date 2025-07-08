from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# Helper function to build a binary tree from a list (level-order input)
def build_tree(values):
    if not values or values[0] is None:
        return None  # Return None if input is empty or root is None

    root = TreeNode(values[0])  # Initialize root
    queue = deque([root])
    i = 1  # Index for iterating the list

    while queue and i < len(values):
        current = queue.popleft()

        # Add left child if available
        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1

        # Add right child if available
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    return root

# Function to perform level-order traversal and find the level with maximum sum
def level_order_traversal(root):
    level = 0  # Track current level (starting from 0)
    max_sum = root.val  # Initialize with root value
    smallest_level = 1  # Since root is at level 1 (1-based index)

    queue = deque([root])
    while queue:
        level_size = len(queue)
        level += 1
        summation = 0  # Sum of values at the current level

        for _ in range(level_size):
            current = queue.popleft()
            summation += current.val

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

        # Update max_sum and level if a new maximum is found
        if max_sum < summation:
            max_sum = summation
            smallest_level = level

    return smallest_level

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        return level_order_traversal(root)

# Example usage
root = [1, 7, 0, 7, -8, None, None]
root = build_tree(root)

sol = Solution()
print(sol.maxLevelSum(root))
