"""
Problem: Excel Sheet Column Title

Approach:
Treat the column number like a base-26 number system (but without zero).
Repeatedly take modulo 26 to get the corresponding character and build
the result string from right to left. Subtract 1 each time to handle
1-based indexing.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""

        while columnNumber > 0:
            columnNumber -= 1
            result = chr(columnNumber % 26 + ord('A')) + result
            columnNumber //= 26

        return result
