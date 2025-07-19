"""
LeetCode Problem: 328. Odd Even Linked List
URL             : https://leetcode.com/problems/odd-even-linked-list/

Description:
    Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices,
    and return the reordered list.

    Note that the relative order inside both the even and odd groups should remain the same.

    The first node is considered odd, the second node even, and so on.

Approach:
    1. If the list is empty or has only one node, return it as is.
    2. Use two pointers — one for odd-indexed nodes and one for even-indexed nodes.
    3. Traverse the list, connecting odd-indexed nodes to each other and even-indexed nodes to each other.
    4. Finally, link the last odd node to the head of the even list.

Time Complexity:
    O(n) — Each node is visited exactly once.

Space Complexity:
    O(1) — The algorithm uses only a constant amount of extra space.

Language: Python
"""

from typing import Optional

# Define a singly linked list node
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

# Function to build a singly linked list from a list of values
def build_list(values):
    if not values:
        return None

    head = ListNode(values[0])   # Create head node
    current = head

    for i in values[1:]: # Append remaining nodes
        current.next = ListNode(i)
        current = current.next

    return head

# Function to display the linked list as a Python list
def display(head):
    if not head:
        return []

    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next

    return result

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If the list has 0 or 1 node, return as is
        if not head or not head.next:
            return head

        odd = head                     # Pointer to build the odd-indexed list
        even = head.next               # Pointer to build the even-indexed list
        even_start = head.next         # Store start of even list to reconnect later

        # Rearranging the nodes by changing links
        while even and even.next:
            odd.next = even.next       # Link current odd node to next odd node
            even.next = even.next.next # Link current even node to next even node

            odd = odd.next             # Move odd pointer
            even = even.next           # Move even pointer

        # Connect the end of odd list to the start of even list
        odd.next = even_start

        return head

# Example usage
head = [1, 2, 3, 4, 5]
head = build_list(head)
print(display(head))           # Original list: [1, 2, 3, 4, 5]

sol = Solution()
head = sol.oddEvenList(head)
print(display(head))           # Modified list: [1, 3, 5, 2, 4]