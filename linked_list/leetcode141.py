"""
LeetCode Problem: 141. Linked List Cycle
URL             : https://leetcode.com/problems/linked-list-cycle/

Description:
    Given head of a singly linked list, determine if the linked list has a cycle in it.
    A cycle occurs if a node can be visited again by continuously following the next pointer.
    The list can have duplicate values, so we must rely on node references (not values).

Approach (Using Hash Set):
    1. Traverse the linked list node by node.
    2. Maintain a set to store references to nodes we’ve already visited.
    3. At each step:
        - If the current node is already in the set, a cycle exists → return True.
        - Otherwise, add the node to the set and move forward.
    4. If we reach the end (null), then there is no cycle.

Why this works:
    - Node values can be duplicated, but node *references* (object identities) are unique.
    - Sets in Python compare object identity, not value, making them perfect for this task.

Time Complexity:
    O(n) — In the worst case, we visit each node once.

Space Complexity:
    O(n) — We store up to n node references in the visited set.

Language: Python
"""

from typing import Optional

# Definition for singly linked list node
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Function to build a linked list from a list of values
# 'pos' indicates the index where the tail connects to form a cycle
# If pos == -1, there is no cycle
def build_list(values, pos):
    if not values:
        return None  # Empty list, return None

    head = ListNode(values[0])  # Create head node

    cycle_node = None           # This will point to the node where cycle starts (if any)
    if pos == 0:
        cycle_node = head       # If cycle at head, set cycle_node here

    current = head
    # Create the rest of the nodes
    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next

        if i == pos:
            cycle_node = current  # Mark cycle start node at position 'pos'

    # If pos != -1, link the last node to the cycle_node to form a cycle
    if pos != -1:
        current.next = cycle_node

    return head

class Solution:
    # Function to detect if linked list has a cycle.
    # Uses a set to store visited nodes.
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head

        # To store visited node references (actual nodes), not their values,
        # because node values can be duplicated, but node identities are unique.
        visited = set()

        while current:
            # If current node is not visited, add it to visited set
            if current not in visited:
                visited.add(current)
                current = current.next
            else:
                # Node already visited, so cycle detected
                return True

        # Reached end of list without revisiting any node, no cycle
        return False

# Example usage
head = [3, 2, 0, -4]
pos = 1
head = build_list(head, pos)  # Builds linked list with cycle at position 1

sol = Solution()
print(sol.hasCycle(head))     # Output: True, since there is a cycle

# ------------------------------ Optimization Approach ------------------------------ #

"""
LeetCode Problem: 141. Linked List Cycle  
URL             : https://leetcode.com/problems/linked-list-cycle/

Description:
    Given the head of a singly linked list, determine if the linked list contains a cycle.
    A cycle occurs if a node can be reached again by continuously following the next pointer.
    Note that the linked list may contain duplicate values, so detection must be based on node
    references (not values).

Approach (Floyd’s Cycle Detection - Tortoise and Hare Algorithm):
    1. Use two pointers, slow and fast.
       - Slow moves one step at a time.
       - Fast moves two steps at a time.
    2. If there is a cycle, the fast pointer will eventually meet the slow pointer.
    3. If fast reaches the end (null), there is no cycle.

Why this works:
    - In a cyclic list, the fast pointer "laps" the slow pointer and they will meet.
    - This method uses constant space, making it optimal for cycle detection.

Time Complexity:
    O(n) — In the worst case, each node is visited at most once.

Space Complexity:
    O(1) — Uses only two pointers regardless of list size.

Alternative Approach (using Hash Set - not used here):
    - Store visited node references in a set.
    - If a node is revisited, a cycle exists.
    - Uses O(n) space.
"""

class Solution:
    # Function to detect if a linked list has a cycle.
    # Uses Floyd’s Cycle Detection Algorithm (also known as Tortoise and Hare).
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head  # Moves one step at a time
        fast = head  # Moves two steps at a time

        # Traverse the list as long as fast and fast.next are not None
        while slow and fast and fast.next:
            slow = slow.next           # Move slow pointer by 1 step
            fast = fast.next.next      # Move fast pointer by 2 steps

            if slow == fast:
                # If both pointers meet, there is a cycle
                return True

        # If fast reaches the end, there is no cycle
        return False