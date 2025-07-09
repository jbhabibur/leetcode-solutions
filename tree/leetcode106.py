from typing import List, Optional

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# Helper function to recursively build the binary tree
def build_tree_recursively(inorder, postorder, start, end, idx):
    # Base case: no elements to construct the subtree
    if start > end:
        return None

    # Get the current root value from postorder using the current index
    root_value = postorder[idx[0]]
    root = TreeNode(root_value)  # Create a new tree node
    idx[0] -= 1  # Move to the next root element (right to left in postorder)

    # Find the index of the root in inorder to divide left and right subtrees
    i = end
    while i >= start and inorder[i] != root_value:
        i -= 1

    # Recursively build right subtree first because postorder is processed from the end
    root.right = build_tree_recursively(inorder, postorder, i + 1, end, idx)
    # Recursively build left subtree
    root.left = build_tree_recursively(inorder, postorder, start, i - 1, idx)

    return root

# Wrapper function to initialize index and start recursive construction
def build_tree(inorder, postorder):
    n = len(postorder)
    idx = [n - 1]  # Start from the last element in postorder (root)
    return build_tree_recursively(inorder, postorder, 0, n - 1, idx)

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return build_tree(inorder, postorder)

# Example usage
inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]

sol = Solution()
print(sol.buildTree(inorder, postorder))
