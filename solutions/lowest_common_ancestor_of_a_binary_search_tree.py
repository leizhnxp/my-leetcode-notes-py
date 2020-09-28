# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def is_full(self):
        if self.left is None:
            return False
        if self.right is None:
            return False
        return True


class Solution:
    def lowest_common_ancestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if p.val > q.val:
            p, q = q, p

        if root.val == p.val:
            return root
        if root.val == q.val:
            return root

        if root.val < p.val:
            return self.lowest_common_ancestor(root.right, p, q)

        if root.val > q.val:
            return self.lowest_common_ancestor(root.left, p, q)
        # if p.val< root.val < q.val:

        return root
