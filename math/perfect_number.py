"""
Problem: Perfect Number

Approach:
Check all divisors up to sqrt(n). If a divisor is found,
add both the divisor and its corresponding pair (num // i).
Start with total = 1 since 1 is always a divisor.
Finally, check if the sum of divisors equals the number.

Time Complexity: O(sqrt(n))
Space Complexity: O(1)
"""

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False

        total = 1

        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                total += i

                if i != num // i:
                    total += num // i

        return total == num
