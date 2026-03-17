"""
Problem: Valid Parentheses

Approach:
Use a stack to keep track of opening brackets. For every closing bracket,
check if it matches the most recent opening bracket in the stack.
If it doesn't match or the stack is empty, return False.
At the end, if the stack is empty, all brackets are valid.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char in mapping:
                top = stack.pop() if stack else '#'

                if mapping[char] != top:
                    return False
            else:
                stack.append(char)

        return not stack
