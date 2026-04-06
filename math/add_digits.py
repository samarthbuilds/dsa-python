"""
Problem: Add Digits

Approach:
Repeatedly sum the digits of the number until it becomes a single digit.
Use a loop to extract each digit using modulo and integer division,
compute the sum, and update the number.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            total = 0
            while num > 0:
                digit = num % 10
                total += digit
                num //= 10
            num = total
        return num
