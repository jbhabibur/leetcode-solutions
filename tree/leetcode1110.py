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

def preorder(current, to_delete, forest):
    if current is None:
        return None

    # Recursively traverse the tree in postorder traversal (children processed first)
    current.left = preorder(current.left, to_delete, forest)
    current.right = preorder(current.right, to_delete, forest)

    # If the current node is not in the to_delete set,
    # it means it should not be deleted, so we return the current node (with its subtree unchanged).
    if current.val not in to_delete:
        return current

    # If the current node is in the to_delete set,
    # we need to check if it has left or right children.
    # If it does, those children become new roots in the forest,
    # so we add them to the forest list.
    if current.left is not None:
        forest.append(current.left)
    if current.right is not None:
        forest.append(current.right)

    # If a node is to be deleted, it should be unlinked from its children and its parent.
    current.left = None
    current.right = None
    return None

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)  # Convert list to set for O(1) average-time lookups
        forest = []
        root = preorder(root, to_delete, forest)

        # If the root itself was not deleted, add it to the forest
        if root:
            forest.append(root)

        return forest

# Example usage
root = [1, 2, 3, 4, 5, 6, 7]
to_delete = [3, 5]
root = build_bt(root)

sol = Solution()
sol.delNodes(root, to_delete)
