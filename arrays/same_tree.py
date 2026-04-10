"""
Problem: Same Tree

Approach:
Use recursion to compare both trees.
If both nodes are null, return True.
If one is null or values differ, return False.
Recursively check left and right subtrees.

Time Complexity: O(n)
Space Complexity: O(h)
"""

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
