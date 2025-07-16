from typing import Optional

# Define a binary tree node
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# Function to build binary search tree (BST) from level-order list
def build_bst(values):
    root = None

    for val in values:
        if val is not None:
            root = insert(root, val)

    return root

def insert(current, val):
    # Base case: when current is None, we create a node,
    # and assign its reference to its parent left or right child
    if current is None:
        return TreeNode(val)

    # If value is smaller than root, recursively going to left subtree
    if val < current.val:
        current.left = insert(current.left, val)

    # If value is greater than root, recursively going to right subtree
    elif val > current.val:
        current.right = insert(current.right, val)

    # After all recursions are done, return the root
    return current

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return insert(root, val)

# Example usage
root = [4, 2, 7, 1, 3]
val = 5
root = build_bst(root)

sol = Solution()
sol.insertIntoBST(root, val)
