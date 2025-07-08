from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(values):
    if not values or values[0] is None:
        return None  # Empty list or root is None means no tree

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1  # Index to track position in values list

    while queue and i < len(values):
        current = queue.popleft()

        # Assign left child if available and not None
        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1

        # Assign right child if available and not None
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    return root

def level_order_traversal(root):
    if not root:
        return []

    levels = []
    queue = deque([root])

    while queue:
        level_size = len(queue)  # Number of nodes in current level
        level = []

        for _ in range(level_size):
            current = queue.popleft()
            level.append(current.val)

            # Add children to queue for next level processing
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        levels.append(level)  # Append current level values to result

    return levels

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Wrapper to call the helper function
        return level_order_traversal(root)

# Example usage
root = [3,9,20,None,None,15,7]
root = build_tree(root)

sol = Solution()
print(sol.levelOrder(root))