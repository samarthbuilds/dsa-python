"""
Problem: Ugly Number

Approach:
An ugly number has only prime factors 2, 3, and 5.
Continuously divide the number by these factors while possible.
If the final result becomes 1, it is an ugly number.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        for factor in [2, 3, 5]:
            while n % factor == 0:
                n //= factor

        return n == 1
