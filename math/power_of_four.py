"""
Problem: Power of Four

Approach:
Continuously divide the number by 4 while it is divisible.
If the final result becomes 1, then the number is a power of four.
Also ensure that the number is positive.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        while n % 4 == 0:
            n //= 4

        return n == 1
