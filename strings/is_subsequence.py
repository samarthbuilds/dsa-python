"""
Problem: Is Subsequence

Approach:
Use two pointers for both strings.
One pointer tracks string s and the other tracks string t.
If characters match, move the pointer of s forward.
Always move the pointer of t forward.
If the pointer of s reaches the end, then s is a subsequence of t.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)
