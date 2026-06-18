"""
Problem: Power of Two

Approach:
Use a bit manipulation trick.
A power of two has exactly one set bit in its binary representation.
For such numbers, n & (n - 1) equals 0.
Also ensure that n is positive.

Time Complexity: O(1)
Space Complexity: O(1)
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0
