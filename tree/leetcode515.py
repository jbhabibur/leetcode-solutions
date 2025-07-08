from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# Helper function to build a binary tree from a level-order list representation
def build_tree(values):
    if not values or values[0] is None:
        return None  # If the input list is empty or root is None, return an empty tree

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        current = queue.popleft()

        # Check if there's a left child at index i
        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1

        # Check if there's a right child at index i
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    return root

# Function to perform level-order traversal and collect maximum value at each level
def level_order_traversal(root):
    if not root:
        return []  # Return empty list if tree is empty

    result = []                # This will store max values level by level
    queue = deque([root])      # Start BFS with the root node

    while queue:
        level_size = len(queue)     # Number of nodes at the current level
        max_value = queue[0].val    # Initialize max value with the first node's value in this level

        for _ in range(level_size):
            current = queue.popleft()

            # Update max_value if current node's value is greater
            if current.val > max_value:
                max_value = current.val

            # Add child nodes to queue for the next level
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        # After finishing this level, append the maximum value found
        result.append(max_value)

    return result  # Return list of largest values from each level

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        return level_order_traversal(root)

# Example usage
root = [1,3,2,5,3,None,9]
root = build_tree(root)

sol = Solution()
print(sol.largestValues(root))
