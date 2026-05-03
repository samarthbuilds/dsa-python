"""
Problem: Repeated Substring Pattern

Approach:
Concatenate the string with itself and remove the first and last characters.
If the original string exists in this modified string, it means the string
can be formed by repeating a substring.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]
