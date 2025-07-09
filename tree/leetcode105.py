from typing import List, Optional

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# Helper function to recursively build the binary tree
def build_tree_recursively(preorder, inorder, start, end, idx):
    # Base case: if there are no elements to construct the tree
    if start > end:
        return None

    # Get the current root value from preorder using the current index
    root_value = preorder[idx[0]]
    root = TreeNode(root_value) # Create a new tree node
    idx[0] = idx[0] + 1 # Move to the next element in preorder

    # Find the index of the current root in inorder to split left and right subtrees
    i = start
    while i <= end and inorder[i] != root_value:
        i += 1

    # Recursively build the left and right subtrees
    root.left = build_tree_recursively(preorder, inorder, start, i - 1, idx)
    root.right = build_tree_recursively(preorder, inorder, i + 1, end, idx)

    return root

# Wrapper function to initialize index and start the recursive building process
def build_tree(preorder, inorder):
    n = len(inorder)
    idx = [0]
    return build_tree_recursively(preorder, inorder, 0, n - 1, idx)

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return build_tree(preorder, inorder)

# Example usage
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

sol = Solution()
print(sol.buildTree(preorder, inorder))
