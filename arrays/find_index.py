"""
Problem: Find the Index of the First Occurrence in a String

Approach:
Iterate through the haystack string and check every possible substring
of length equal to the needle. If the substring matches the needle,
return the starting index. If no match is found, return -1.

Time Complexity: O(n * m)
Space Complexity: O(1)
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        for i in range(n - m + 1):
            if haystack[i:i+m] == needle:
                return i

        return -1
