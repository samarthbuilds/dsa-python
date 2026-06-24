"""
Problem: Find the Pivot Integer

Approach:
Calculate the sum of numbers from 1 to n.
If this sum is a perfect square, then its square root
is the pivot integer. Otherwise, no pivot integer exists.

Time Complexity: O(1)
Space Complexity: O(1)
"""

class Solution:
    def pivotInteger(self, n: int) -> int:
        total = n * (n + 1) // 2

        root = int(total ** 0.5)

        if root * root == total:
            return root

        return -1
