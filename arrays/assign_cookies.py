"""
Problem: Assign Cookies

Approach:
Sort both the greed factors and cookie sizes.
Use two pointers to match the smallest available cookie
that can satisfy the current child. If a cookie satisfies
the child, move to the next child. Always move to the next cookie.
The number of satisfied children is the answer.

Time Complexity: O(n log n + m log m)
Space Complexity: O(1)
"""

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        child = 0
        cookie = 0

        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                child += 1

            cookie += 1

        return child
