"""
Problem: Base 7

Approach:
Repeatedly divide the number by 7 and store the remainder.
Build the result string in reverse order. Handle negative
numbers separately by storing the sign and converting the
absolute value.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        negative = num < 0
        num = abs(num)
        result = ""

        while num > 0:
            result = str(num % 7) + result
            num //= 7

        if negative:
            result = "-" + result

        return result
