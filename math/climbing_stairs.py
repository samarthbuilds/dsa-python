"""
Problem: Climbing Stairs

Approach:
This is a Fibonacci-like problem.
The number of ways to reach step n is the sum of ways to reach (n-1) and (n-2).
Use two variables to store previous results and iteratively compute the answer.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev2 = 1
        prev1 = 2

        for i in range(3, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr

        return prev1
