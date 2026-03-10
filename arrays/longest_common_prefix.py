"""
Problem: Longest Common Prefix

Approach:
Use the first string as a reference. Iterate through each character
position of the first string and compare it with the same position
in all other strings. If a mismatch is found or the index exceeds the
length of any string, return the prefix up to that point.

Time Complexity: O(n * m)
Space Complexity: O(1)
"""

class Solution:
    def longestCommonPrefix(self, strs): 
        if not strs:
            return " "

        for i in range(len(strs[0])):
            char = strs[0][i]

            for s in strs[1:]:
                if i >= len(s) or s[i] != char:
                    return strs[0][:i]

        return strs[0]
