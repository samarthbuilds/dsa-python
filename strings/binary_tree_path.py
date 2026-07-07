"""
Problem: Binary Tree Paths

Approach:
Use Depth First Search (DFS) with recursion.
Maintain the current path as a string while traversing the tree.
When a leaf node is reached, add the complete path to the result.
Otherwise, continue exploring the left and right subtrees.

Time Complexity: O(n)
Space Complexity: O(h)
"""

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []

        def dfs(node, path):
            if not node:
                return

            path += str(node.val)

            if not node.left and not node.right:
                result.append(path)
                return

            path += "->"
            dfs(node.left, path)
            dfs(node.right, path)

        dfs(root, "")

        return result
