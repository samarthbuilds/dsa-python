"""
Problem: Count Binary Substrings

Approach:
Count the lengths of consecutive groups of identical characters.
Whenever the character changes, add the minimum of the previous
group length and the current group length to the answer.
After processing the string, add the contribution of the last group.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev_group = 0
        curr_group = 1
        ans = 0

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr_group += 1

            else:
                ans += min(prev_group, curr_group)
                prev_group = curr_group
                curr_group = 1

        ans += min(prev_group, curr_group)
        return ans
