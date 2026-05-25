"""
Problem: Jewels and Stones

Approach:
Store all jewel characters in a set for fast lookup.
Iterate through the stones string and count how many
characters are present in the jewel set.

Time Complexity: O(n)
Space Complexity: O(k)
"""

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)
        count = 0

        for ch in stones:
            if ch in jewel_set:
                count += 1

        return count
