"""
Problem: Length of Last Word

Approach:
Start from the end of the string and skip any trailing spaces.
Then count the length of characters until a space is encountered
or the string ends. That count is the length of the last word.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        i = len(s) - 1

        while i >= 0 and s[i] == ' ':
            i -= 1

        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1

        return length
