"""
Problem: Fibonacci Number

Approach:
Use an iterative dynamic programming approach.
Keep track of the previous two Fibonacci numbers and
update them step by step to compute the nth number.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        prev2 = 0
        prev1 = 1

        for i in range(2, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr

        return prev1
