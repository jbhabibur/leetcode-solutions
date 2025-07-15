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

# Inorder traversal: left → root → right
def inorder(current):
    if current:
        inorder(current.left)
        print(current.val)
        inorder(current.right)

def dfs(current):
    # Base case: if the current node is None, return None (nothing to invert)
    if current is None:
        return None

    # Swap left and right children
    current.left, current.right = current.right, current.left

    # Recursively invert left and right subtrees
    dfs(current.left)
    dfs(current.right)

    return current

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root = dfs(root)

        return root

# Example usage
root = [4, 2, 7, 1, 3, 6, 9]
root = build_binary_tree(root)

sol = Solution()
root = sol.invertTree(root)
inorder(root)