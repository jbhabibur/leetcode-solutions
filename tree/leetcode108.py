"""
LeetCode Problem: 108. Convert Sorted Array to Binary Search Tree
URL             : https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

Description:
    Given an integer array nums where the elements are sorted in ascending order,
    convert it to a height-balanced binary search tree.

Approach:
    1. Find the middle element of the current array segment as the root node.
    2. Recursively build the left subtree using the left half of the array.
    3. Recursively build the right subtree using the right half of the array.
    4. Use recursion until the base case of an empty array is reached.

Time Complexity:
    O(n) — Each element is processed once in the recursion.

Space Complexity:
    O(log n) — Due to recursive call stack in a balanced BST.

Language: Python
"""

from typing import List, Optional

# Definition for binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Base case: empty list means no tree node
        if not nums:
            return None

        # Find middle index to select root value
        middle_index = len(nums) // 2
        root = TreeNode(nums[middle_index])

        # Recursively build the left subtree from the left half of the list
        root.left = self.sortedArrayToBST(nums[:middle_index])

        # Recursively build the right subtree from the right half of the list
        root.right = self.sortedArrayToBST(nums[middle_index + 1:])

        # Return the root node of this subtree
        return root
