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

def preorder(current, target,path, result):
    if current is None:
        return None

    path.append(current.val)

    current.left = preorder(current.left, target, path, result)
    current.right = preorder(current.right, target, path, result)

    if current.left is None and current.right is None and sum(path) == target:
        # Append a copy of the current path to the result list.
        # Since 'path' is mutable and will be modified during backtracking,
        # copying it ensures the stored path remains intact and unaffected by future changes.
        result.append(path[:])

    # Remove the last element from path to backtrack,
    # restoring path to its previous state before exploring other branches.
    path.pop()

    return current

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        path = []
        preorder(root, targetSum, path, result)

        return result

# Example usage
root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
targetSum = 22
root = build_bt(root)

sol = Solution()
root = sol.pathSum(root, targetSum)