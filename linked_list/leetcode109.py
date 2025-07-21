"""
LeetCode Problem: 109. Convert Sorted List to Binary Search Tree
URL             : https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

Description:
    Given the head of a singly linked list where elements are sorted in ascending order,
    convert it to a height-balanced binary search tree.

Approach:
    1. Use the two-pointer technique (slow and fast) to find the middle node of the list.
    2. That middle node becomes the root of the BST.
    3. Recursively do the same for the left half (before mid) and right half (after mid).
    4. Disconnect the left half by setting prev.next = None.

Time Complexity:
    O(n log n) — Each recursive call finds the middle node in O(n), and there are log n levels.

Space Complexity:
    O(log n) — Due to recursive call stack.

Language: Python
"""

from typing import Optional

# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def find_middle_node(self, head: ListNode) -> ListNode:
        """
        Uses slow and fast pointers to find the middle node.
        Also splits the list into two halves by disconnecting at mid.
        """

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Split the list into two halves
        if prev:
            prev.next = None

        return slow

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        """
        Recursively builds a height-balanced BST from the sorted linked list.
        """

        # Base case 1: empty list
        if head is None:
            return None

        # Base case 2: single node becomes a leaf TreeNode
        if head.next is None:
            return TreeNode(head.val)

        # Get the middle node to use as root
        middle_node = self.find_middle_node(head)
        root = TreeNode(middle_node.val)

        # Recursively construct left subtree from left half
        root.left = self.sortedListToBST(head)

        # Recursively construct right subtree from right half
        root.right = self.sortedListToBST(middle_node.next)

        return root