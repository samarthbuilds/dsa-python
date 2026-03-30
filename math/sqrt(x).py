"""
Problem: Sqrt(x)

Approach:
Use binary search to find the integer square root.
Search in the range from 1 to x//2 and check mid * mid.
If mid * mid equals x, return mid.
If it's smaller, move left forward.
If it's larger, move right backward.
Finally, return the largest integer whose square is less than or equal to x.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left = 1
        right = x // 2

        while left <= right:
            mid = (left + right) // 2

            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1

        return right
