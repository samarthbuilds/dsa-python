"""
Problem: Convert a Number to Hexadecimal

Approach:
Use repeated division by 16 to convert the number into hexadecimal.
For negative numbers, convert using 32-bit two's complement by adding 2^32.
Map each remainder to its corresponding hexadecimal character.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        hex_chars = "0123456789abcdef"

        if num < 0:
            num += 2**32

        result = ""

        while num > 0:
            result = hex_chars[num % 16] + result
            num //= 16

        return result
