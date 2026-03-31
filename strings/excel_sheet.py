"""
Problem: Excel Sheet Column Number

Approach:
Treat the column title as a base-26 number system.
For each character, convert it to its corresponding value
(A=1, B=2, ..., Z=26) and update the result by multiplying
the current result by 26 and adding the value.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0

        for ch in columnTitle:
            value = ord(ch) - ord('A') + 1
            result = result * 26 + value

        return result
