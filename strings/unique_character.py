"""
Problem: First Unique Character in a String

Approach:
Use a hashmap to count the frequency of each character in the string.
Then iterate through the string again and return the index of the first
character with frequency 1. If no such character exists, return -1.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        for i in range(len(s)):
            if count[s[i]] == 1:
                return i

        return -1
