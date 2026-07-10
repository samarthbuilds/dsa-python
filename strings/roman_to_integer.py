"""
Problem: Roman to Integer

Approach:
Use a hashmap to store the value of each Roman numeral.
Traverse the string from left to right. If the current numeral
is smaller than the next one, subtract its value; otherwise,
add its value. The final total is the integer representation.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0

        for i in range(len(s)):
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]

        return total
