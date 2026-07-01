"""
Problem: Longest Substring Without Repeating Characters

Approach:
Use the sliding window technique with a set to track unique characters.
Expand the window by moving the right pointer.
If a duplicate character is found, shrink the window from the left
until all characters in the window are unique.
Track the maximum window size throughout the process.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        ans = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            ans = max(ans, right - left + 1)

        return ans
