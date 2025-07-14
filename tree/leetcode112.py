from typing import Optional, List
from collections import deque

# Define binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
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

def dfs(current, target, path):
    if current is None:
        return False

    path.append(current.val)

    # Check if it's a leaf and the sum matches target
    if current.left is None and current.right is None and sum(path) == target:
        return True

    # Explore left and right subtrees
    if dfs(current.left, target, path):
        return True
    if dfs(current.right, target, path):
        return True

    # Remove the last element from path to backtrack,
    # restoring path to its previous state before exploring other branches.
    path.pop()

    return False

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        path = []
        return dfs(root, targetSum, path)

# Example usage
root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
targetSum = 22
root = build_bt(root)

sol = Solution()
print(sol.hasPathSum(root, targetSum))
