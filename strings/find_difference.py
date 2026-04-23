"""
Problem: Find the Difference

Approach:
Use a hashmap to count the frequency of characters in string s.
Then iterate through string t and decrease the count.
If a character is not found in the hashmap or its count becomes zero,
that character is the extra one.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        for ch in t:
            if ch not in count or count[ch] == 0:
                return ch
            count[ch] -= 1
