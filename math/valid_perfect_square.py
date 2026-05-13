"""
Problem: Valid Perfect Square

Approach:
Use binary search to find whether a number's square root exists as an integer.
Search in the range from 1 to num and compare mid * mid with num.
If a match is found, return True. Otherwise adjust the search range accordingly.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            if square == num:
                return True

            elif square < num:
                left = mid + 1

            else:
                right = mid - 1

        return False
