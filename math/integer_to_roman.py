"""
Problem: Integer to Roman

Approach:
Use a greedy approach with predefined value-symbol pairs.
Start from the largest value and subtract it from the number
while appending the corresponding Roman symbol to the result.
Continue until the number becomes zero.

Time Complexity: O(1)
Space Complexity: O(1)
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        values = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]

        result = ""

        for value, symbol in values:
            while num >= value:
                result += symbol
                num -= value

        return result
