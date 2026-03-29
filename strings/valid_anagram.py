"""
Problem: Valid Anagram

Approach:
Sort both strings and compare them. If they are equal after sorting,
they are anagrams of each other.

Time Complexity: O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
