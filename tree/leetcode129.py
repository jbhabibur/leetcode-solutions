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

def preorder(current, path, result):
    # Base case: if current node is None, return
    if current is None:
        return None

    # Add current node's value to the path
    path.append(current.val)

    current.left = preorder(current.left, path, result)
    current.right = preorder(current.right, path, result)

    # If it's a leaf node, convert path to integer and store in result
    if not current.left and not current.right:
        number = int("".join(map(str, path[:])))
        result.append(number)

    # Backtrack: remove the last node from path
    path.pop()

    return current

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        path = []
        result = []
        preorder(root, path, result)

        # Sum of all root-to-leaf numbers
        return sum(result)

# Example usage
root = [4, 9, 0, 5, 1]
root = build_bt(root)

sol = Solution()
print(sol.sumNumbers(root))