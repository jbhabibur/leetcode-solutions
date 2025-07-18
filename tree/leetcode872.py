"""
LeetCode Problem: 872. Leaf-Similar Trees
URL             : https://leetcode.com/problems/leaf-similar-trees/

Description:
    Given the roots of two binary trees, determine whether their leaf value
    sequences (from left to right) are the same.

Approach:
    1. A leaf node is defined as a node with no left or right child.
    2. Use Depth-First Search (DFS) to collect the leaf values from each tree
       in left-to-right order.
    3. Compare the resulting leaf sequences for equality.

Time Complexity:
    O(n + m), where n and m are the number of nodes in the two trees.

Space Complexity:
    O(h) for the recursion stack (h = max height of the trees),
    O(L) for storing leaf values (L = number of leaves).

Language: Python
"""

from typing import Optional
from collections import deque

# Define a binary tree node
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# Function to build binary tree from level-order list
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

# DFS to collect leaf node values
def dfs(current, leaf_nodes):
    if current is None:
        return
    if current.left is None and current.right is None:
        leaf_nodes.append(current.val)  # Add leaf value
        return
    dfs(current.left, leaf_nodes)
    dfs(current.right, leaf_nodes)

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf_nodes1 = []  # Leaf values from root1
        leaf_nodes2 = []  # Leaf values from root2

        dfs(root1, leaf_nodes1)
        dfs(root2, leaf_nodes2)

        return leaf_nodes1 == leaf_nodes2  # Compare leaf sequences

# Example usage
root1 = [3,5,1,6,2,9,8,None,None,7,4]
root2 = [3,5,1,6,7,4,2,None,None,None,None,None,None,9,8]
root1 = build_bt(root1)
root2 = build_bt(root2)

sol = Solution()
print(sol.leafSimilar(root1, root2))