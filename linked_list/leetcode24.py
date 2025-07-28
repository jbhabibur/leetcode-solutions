"""
LeetCode Problem: 24. Swap Nodes in Pairs
URL             : https://leetcode.com/problems/swap-nodes-in-pairs/

Description:
    Given a singly linked list, swap every two adjacent nodes and return its head.
    You must solve the problem without modifying the values in the list's nodes
    (i.e., only nodes themselves may be changed.)

Approach:
    1. Use recursion to swap every pair of adjacent nodes.
    2. Base case: If the list has 0 or 1 node, return the head.
    3. Recursive case:
        - Let `first` and `second` be the first two nodes.
        - Point `first.next` to the result of swapping the rest of the list.
        - Point `second.next` to `first`.
        - Return `second` as the new head of the pair.

Time Complexity:
    O(n) — Each node is visited once.

Space Complexity:
    O(n) — Due to recursive stack frames.

Language: Python
"""

from typing import Optional

# Define a singly linked list node
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Function to build a singly linked list from a list
def build_list(values):
    # Case 1: If input list is empty, return None
    if not values:
        return None

    # Case 2: If input list is not empty – build the linked list
    head = ListNode(values[0])  # Initialize the head node with the first value
    current = head

    # Iterate through the remaining values and create linked nodes
    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next

    return head

# Function to convert a linked list into a list of values
def display(head):
    # Case 1: If the linked list is empty, return an empty list
    if not head:
        return []

    # Case 2: If the linked list is not empty – traverse and collect node values
    result = []
    current = head
    while current:  # Iterate until the end of the linked list
        result.append(current.val)
        current = current.next

    return result

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base Case 1: If the list is empty, there is nothing to swap
        if head is None:
            return None

        # Base Case 2: If there is only one node, no swap needed
        if head.next is None:
            return head

        # Step 1: Identify the first and second nodes to be swapped
        first = head
        second = head.next

        # Step 2: Recursively call swapPairs on the rest of the list starting from the node after the second
        first.next = self.swapPairs(second.next)

        # Step 3: Swap the first and second nodes
        second.next = first

        # Step 4: Return the new head of this pair (which is second after swapping)
        return second

# Example usage
head = []
head = build_list(head)
print(display(head))

sol = Solution()
head = sol.swapPairs(head)
print(display(head))