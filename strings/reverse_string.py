"""
Problem: Reverse String

Approach:
Use two pointers, one at the beginning and one at the end.
Swap the characters at these positions and move both pointers
towards the center until they meet.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
