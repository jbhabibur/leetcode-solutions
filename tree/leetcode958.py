from typing import  Optional
from collections import deque

# Define a binary tree node
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# Build the binary tree from the level order traversal
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

        # Right right
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    return root

def bfs(root):
    queue = deque([root])
    flag = False

    while queue:
        current = queue.popleft()

        if current is None:
            flag = True
        else:
            if flag:
                return False # A binary tree is not a complete binary tree if any node comes after a None
            queue.append(current.left)
            queue.append(current.right)

    return True

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        return bfs(root)

# Example usage
root = [1, 2, 3, 5, None, 7, 8]
root = build_bt(root)

sol = Solution()
print(sol.isCompleteTree(root))