"""
Problem: Isomorphic Strings

Approach:
Use two hashmaps to maintain a one-to-one mapping
between characters of both strings.
If any mapping conflicts, return False.
Otherwise, continue until all characters are processed.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}

        for c1, c2 in zip(s, t):
            if c1 in s_to_t:
                if s_to_t[c1] != c2:
                    return False
            else:
                s_to_t[c1] = c2

            if c2 in t_to_s:
                if t_to_s[c2] != c1:
                    return False
            else:
                t_to_s[c2] = c1

        return True
