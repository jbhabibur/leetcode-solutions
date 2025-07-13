from typing import Optional, List
from collections import deque

# Define binary tree node
class TreeNode:
    def __init__(self,  val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# Build binary tree from level order traversal
def build_bt(values):
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        current = queue.popleft()

        # Left child
        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1

        # Right child
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    return root

def level_order_traversal(root):
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        current = queue.pop(0)
        if current:
            result.append(current.val)
            queue.append(current.left)
            queue.append(current.right)
        else:
            result.append(None)

    # Optional: Trim trailing Nones for cleaner output
    while result and result[-1] is None:
        result.pop()

    return result

def postorder(current):
    # Base case: if current node is None, return None
    if current is None:
        return None

    # Recursively traverse the tree in postorder traversal (children processed first)
    current.left = postorder(current.left)
    current.right = postorder(current.right)

    # If current node is a leaf with value 0, prune it by returning None
    if current.val == 0 and current.left is None and current.right is None:
        return None

    # Otherwise, return the current node (possibly updated)
    return current

class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root = postorder(root)

        return root

# Example usage
root = [1,0,1,0,0,0,1]
root = build_bt(root)

sol = Solution()
root = sol.pruneTree(root)
print(level_order_traversal(root))
