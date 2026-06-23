"""
Problem: Largest Substring Between Two Equal Characters

Approach:
Use a hashmap to store the first occurrence index of each character.
When the same character appears again, calculate the length of the
substring between the two occurrences and update the maximum length.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first = {}
        ans = -1

        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i

            else:
                ans = max(ans, i - first[ch] - 1)

        return ans
