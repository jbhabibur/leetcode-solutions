"""
LeetCode Problem: 237. Delete Node in a Linked List
URL             : https://leetcode.com/problems/delete-node-in-a-linked-list/

Description:
    Write a function to delete a node (except the tail) in a singly linked list,
    given only access to that node.

Approach:
    1. Since we do not have access to the head of the linked list,
       we cannot traverse the list normally.
    2. Instead, copy the value from the next node into the current node.
    3. Then delete the next node by skipping it in the linked list.

Time Complexity:
    O(1) — The deletion operation is done in constant time.

Space Complexity:
    O(1) — No extra space is required.

Language: Python
"""

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

# Function to find and return the first node with the given value
def find_node(head, val):
    # Case 1: If the linked list is empty, return None
    if not head:
        return None

    # Case 2: If the linked list is not empty, traverse the list to find the node with the given value
    current = head
    while current:
        if current.val == val:
            return current  # Return the node if value matches
        current = current.next

    # Value not found in the list
    return None

class Solution:
    def deleteNode(self, node):
        # Copy the value of the next node into the current node
        # Then, bypass the next node
        node.val = node.next.val
        node.next = node.next.next

# Example usage
head = [4, 5, 1, 9]
node = 5
head = build_list(head)
print(display(head))
node = find_node(head, node)

sol = Solution()
sol.deleteNode(node)
