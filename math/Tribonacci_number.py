"""
Problem: N-th Tribonacci Number

Approach:
Use an iterative dynamic programming approach.
Keep track of the previous three Tribonacci numbers and
update them in each iteration to compute the next value.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0

        if n == 1 or n == 2:
            return 1

        a, b, c = 0, 1, 1

        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c

        return c
