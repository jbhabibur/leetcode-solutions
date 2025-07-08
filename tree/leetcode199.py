from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
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

# Perform level order traversal and collect the last (rightmost) node from each level
def level_order_traversal(root):
    if not root:
        return []

    result = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        right_child = None  # To store the rightmost node value of current level

        for _ in range(level_size):
            current = queue.popleft()
            right_child = current.val  # Will be overwritten until last node in level

            # Enqueue children for next level
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        # Add the last node value from this level
        result.append(right_child)

    return result

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        return level_order_traversal(root)

# Example usage
root = [1,2,3,None,5,None,4]
root = build_tree(root)

sol = Solution()
print(sol.rightSideView(root))