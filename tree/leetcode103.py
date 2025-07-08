from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Helper function to build a binary tree from a list (level-order)
def build_tree(values):
    if not values or values[0] is None:
        return None  # Return None if input list is empty or root is None

    root = TreeNode(values[0])
    queue = deque([root])  # Queue for level-order insertion
    i = 1  # Index for traversing the list

    while queue and i < len(values):
        current = queue.popleft()

        # Insert left child
        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1

        # Insert right child
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    return root

# Function to perform zigzag (spiral) level order traversal
def level_order_traversal(root):
    if not root:
        return []  # Return empty list if tree is empty

    result = []
    level = -1  # Track the current level number
    queue = deque([root])  # Queue for BFS traversal

    while queue:
        level_size = len(queue)  # Number of nodes at current level
        level += 1
        nodes = []

        for _ in range(level_size):
            current = queue.popleft()
            nodes.append(current.val)  # Collect node values

            # Add children to queue for next level
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        # Append values in normal order for even levels, reversed for odd
        if level % 2 == 0:
            result.append(nodes)
        else:
            result.append(nodes[::-1])

    return result

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return level_order_traversal(root)

# Example usage
root = [3, 9, 20, None, None, 15, 7]
root = build_tree(root)

sol = Solution()
print(sol.zigzagLevelOrder(root))  # Output: [[3], [20, 9], [15, 7]]
