"""
LeetCode Problem: 2095. Delete the Middle Node of a Linked List
URL             : https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

Description:
    Given the head of a singly linked list, delete the middle node and return the head
    of the modified list. The middle node is defined as the node at index ⌊n / 2⌋
    (0-based indexing), where n is the number of nodes in the list.

    If the list has only one node, return None after deletion.

Approach:
    1. First, traverse the entire list to count the total number of nodes (n).
    2. If n == 1, return None.
    3. Compute the middle index as n // 2.
    4. Traverse the list again to reach the node just before the middle node.
    5. Modify the pointer of the previous node to skip the middle node.

Time Complexity:
    O(n) — Two passes through the list: one to count nodes, one to delete the middle node.

Space Complexity:
    O(1) — No extra space is used; only pointers and counters are maintained.

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
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # First Pass: Count total number of nodes
        count = 0
        current = head
        while current:
            count += 1
            current = current.next

        # Special case: if only one node, return None
        if count == 1:
            return None

        # Second Pass: Traverse to the node before the middle
        middle = count // 2
        current = head
        prev = None
        current_position = 0

        while current_position < middle:
            current_position += 1
            prev = current
            current = current.next

        # Delete the middle node
        prev.next = current.next

        return head

# Example usage
# head = [1, 3, 4, 7, 1, 2, 6]
head = [2]
head = build_list(head)
print(display(head))

sol = Solution()
head = sol.deleteMiddle(head)
print(display(head))


# ------------------------------ Optimization Approach ------------------------------ #


"""
LeetCode Problem: 2095. Delete the Middle Node of a Linked List
URL             : https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

Description:
    Given the head of a singly linked list, delete the middle node and return the head
    of the modified list. The middle node is defined as the node at index ⌊n / 2⌋
    (0-based indexing), where n is the number of nodes in the list.

    If the list has only one node, return None after deletion.

Approach:
    1. Use two pointers: 'slow' and 'fast'. Initialize both at the head.
    2. Move 'fast' by two steps and 'slow' by one step in each iteration.
    3. Keep track of the node before 'slow' (called 'prev').
    4. When 'fast' reaches the end, 'slow' will point to the middle node.
    5. Remove the middle node by setting 'prev.next = slow.next'.
    6. If the list contains only one node, return None.

Time Complexity:
    O(n) — Only one pass through the list is required.

Space Complexity:
    O(1) — No additional data structures are used.

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
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If the list has only one node, deleting the middle node
        # results in an empty list, so return None
        if head.next is None:
            return None

        # Initialize three pointers:
        # slow: will eventually point to the middle node
        # fast: moves twice as fast as slow to find the middle
        # prev: keeps track of the node before slow for deletion
        slow = head
        fast = head
        prev = None

        # Move fast by two steps and slow by one step
        # When fast reaches the end, slow will be at the middle node
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Delete the middle node by skipping it
        # Link prev's next to slow's next, removing slow from the list
        prev.next = slow.next

        return head

# Example usage
head = [1, 3, 4, 7, 1, 2, 6]
# head = [2]
head = build_list(head)
print(display(head))

sol = Solution()
head = sol.deleteMiddle(head)
print(display(head))
