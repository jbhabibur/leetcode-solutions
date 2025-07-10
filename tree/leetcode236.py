from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(values):
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

def find_node(root, val):
    if root is None:
        return None

    if root.val == val:
        return root

    left = find_node(root.left, val)
    if left:
        return left

    right = find_node(root.right, val)
    if right:
        return right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case 1: If root is None, return None
        if root is None:
            return None

        # Base case 2: If root is found either p or q, return root
        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If p and q are found in left and right subtree, root is ancestor
        if left and right:
            return root

        # If left and right both are None, return None
        # If left is found return left or if right is found return right
        return left if left else right

# Example usage
root = [3,5,1,6,2,0,8,None,None,7,4]
p = 5
q = 1
root = build_tree(root)
p_node = find_node(root, p)
q_node = find_node(root, q)

sol = Solution()
print(sol.lowestCommonAncestor(root, p_node, q_node).val)