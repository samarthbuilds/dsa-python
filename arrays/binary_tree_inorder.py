"""
Problem: Binary Tree Inorder Traversal

Approach:
Use Depth First Search (DFS) with recursion.
Traverse the left subtree, then visit the node,
and finally traverse the right subtree (Left → Root → Right).

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)

        dfs(root)

        return result
