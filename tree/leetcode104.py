from typing import Optional
from collections import deque

# Define a binary tree node
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# Function to build binary tree from level-order list
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

def dfs(current, depth, max_depth):
    # Base case: if the current node is None, do nothing
    if current is None:
        return None

    # Update the max_depth[0] if the current depth is greater
    max_depth[0] = max(max_depth[0], depth)

    # Recursively visit the left and right subtrees with increased depth
    dfs(current.left, depth + 1, max_depth)
    dfs(current.right, depth + 1, max_depth)

    # Return the list holding the maximum depth
    return max_depth

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # If the tree is empty, its depth is 0
        if not root:
            return 0

        # Start DFS with depth 1 and a list holding the current max depth
        # We use a list so it can be modified inside recursive calls
        result = dfs(root, 1, [0])

        # Return the final maximum depth from the list
        return result[0]

# Example usage
root = []
root = build_bt(root)

sol = Solution()
print(sol.maxDepth(root))