class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def insert_node(root, val):
    if root is None:
        return TreeNode(val)

    if val < root.val:
        root.left = insert_node(root.left, val)
    elif val > root.val:
        root.right = insert_node(root.right, val)

    return root

def build_bst(values):
    if not values or values[0] is None:
        return None

    root = None
    for val in values:
        if val is not None:
            root = insert_node(root, val)

    return root

def find_node(root, val):
    if root is None:
        return None

    if root.val == val:
        return root
    elif val < root.val:
        return find_node(root.left, val)
    else:
        return find_node(root.right, val)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            # If both p and q are smaller than root, LCA must be in the left subtree
            if p.val < root.val and q.val < root.val:
                root = root.left

            # If both p and q are greater than root, LCA must be in the right subtree
            elif p.val > root.val and q.val > root.val:
                root = root.right

            # If p and q are on different sides (or one equals root), current node is the LCA
            else:
                return root

root = [6,2,8,0,4,7,9,None,None,3,5]
p = 2
q = 8
root = build_bst(root)
p_node = find_node(root, p)
q_node = find_node(root, q)

sol = Solution()
sol.lowestCommonAncestor(root, p_node, q_node)

