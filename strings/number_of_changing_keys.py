"""
Problem: Number of Changing Keys

Approach:
Convert the string to lowercase so that uppercase and lowercase
versions of the same character are treated equally.
Traverse the string and count how many times the current character
differs from the previous one.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        count = 0

        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                count += 1

        return count
