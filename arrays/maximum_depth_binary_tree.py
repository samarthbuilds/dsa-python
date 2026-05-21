"""
Problem: Maximum Depth of Binary Tree

Approach:
Use recursion to calculate the depth of the left and right subtrees.
The depth of the current node is 1 plus the maximum depth
between the left and right subtree.

Time Complexity: O(n)
Space Complexity: O(h)
"""

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)
