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

def level_order_traversal(root):
    if not root:
        return []

    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val if node else None)

        if node:
            queue.append(node.left)
            queue.append(node.right)

    # Remove trailing Nones
    while result and result[-1] is None:
        result.pop()

    return result

def dfs(current, val, depth, level):
    # Base case: if current node is None, just return (nothing to do)
    if current is None:
        return None

    # If we've reached the level right before the target depth,
    # it's time to add the new row of nodes.
    if level == depth - 1:
        # Create a new node with value 'val' and set the current left subtree as its left child
        current.left = TreeNode(val, current.left)

        # Create another new node with value 'val' and set the current right subtree as its right child
        current.right = TreeNode(val, None, current.right)

        # Return after insertion
        return None

    dfs(current.left, val, depth, level + 1)
    dfs(current.right, val, depth, level + 1)

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # Special case: if depth is 1,
        # create a new root node with value 'val' and set the entire original tree as its left child
        if depth == 1:
            return TreeNode(val, root)

        # Otherwise, call DFS starting from the root at level 1 to add new row at 'depth'
        dfs(root, val, depth, 1)

        # Return the (possibly unchanged) root node of the tree
        return root

# Example usage
root = [4, 2, 6, 3, 1, 5]
val = 1
depth = 2
root = build_binary_tree(root)

sol = Solution()
root = sol.addOneRow(root, val, depth)
print(level_order_traversal(root))