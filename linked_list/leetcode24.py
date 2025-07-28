"""
LeetCode Problem: 24. Swap Nodes in Pairs
URL             : https://leetcode.com/problems/swap-nodes-in-pairs/

Description:
    Given a singly linked list, swap every two adjacent nodes and return its head.
    You must solve the problem without modifying the values in the list's nodes
    (i.e., only nodes themselves may be changed.)

Approach (using recursion):
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
        # Base case: if list is empty, return None
        if head is None:
            return None

        # Base case: if only one node, no need to swap
        if head.next is None:
            return head

        # Identify the first and second nodes in the pair
        first = head
        second = head.next

        # Re-link first to the node after second (i.e., third node)
        first.next = second.next

        # Link second to first (swapping them)
        second.next = first

        # Recurse on the rest of the list starting from the node after the current pair
        head.next = self.swapPairs(first.next)

        # Return the new head (which is second after swap)
        return second

# Example usage
head = []
head = build_list(head)
print(display(head))

sol = Solution()
head = sol.swapPairs(head)
print(display(head))


# ------------------------------ Optimization Approach ------------------------------ #


"""
Approach (using iteration with constant space):
    1. Use iteration with a dummy node to simplify edge cases.
    2. Traverse the list while there are at least two nodes ahead.
    3. Swap the two adjacent nodes by adjusting the 'next' pointers.
    4. Move the pointer forward by two nodes to process the next pair.

Time Complexity:
    O(n) — Each node is visited once.

Space Complexity:
    O(1) — Constant space used, no recursion.

"""

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head

        # Pointer to track the current node before the pair to be swapped
        current = dummy

        # Traverse the list while there are at least two nodes ahead to swap
        while current.next and current.next.next:
            # Identify the two nodes to swap
            first = current.next
            second = current.next.next

            # Swap the nodes by re-pointing their next references
            first.next = second.next
            second.next = first

            current.next = second     # Current now points to second (the new front of the pair)

            # Move the current pointer forward by two nodes to process the next pair
            current = first

        # Return the new head of the list
        return dummy.next