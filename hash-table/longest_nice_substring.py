"""
Problem: Longest Nice Substring

Approach:
Generate all possible substrings and maintain a set of characters
present in the current substring. A substring is considered nice if
for every character, both its lowercase and uppercase versions exist
in the set. Track the longest such substring found.

Time Complexity: O(n^3)
Space Complexity: O(n)
"""

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ans = ""

        for i in range(len(s)):
            chars = set()

            for j in range(i, len(s)):
                chars.add(s[j])
                nice = True

                for ch in chars:
                    if ch.swapcase() not in chars:
                        nice = False
                        break

                if nice and (j - i + 1) > len(ans):
                    ans = s[i:j + 1]

        return ans
