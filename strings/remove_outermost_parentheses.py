"""
Problem: Remove Outermost Parentheses

Approach:
Use a depth counter to track the nesting level of parentheses.
For every opening bracket, add it only if the current depth is greater than 0.
For every closing bracket, decrease the depth first and add it only if
the updated depth is greater than 0.
This removes the outermost parentheses of every primitive substring.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        depth = 0

        for ch in s:
            if ch == '(':
                if depth > 0:
                    result.append(ch)

                depth += 1

            else:
                depth -= 1

                if depth > 0:
                    result.append(ch)

        return "".join(result)
