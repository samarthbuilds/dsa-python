"""
Problem: Power of Three

Approach:
Continuously divide the number by 3 while it is divisible.
If the final result becomes 1, then the number is a power of three.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        while n % 3 == 0:
            n //= 3

        return n == 1
