"""
Problem: Fizz Buzz

Approach:
Iterate from 1 to n and check divisibility conditions.
If a number is divisible by both 3 and 5, append "FizzBuzz".
If divisible only by 3, append "Fizz".
If divisible only by 5, append "Buzz".
Otherwise, append the number as a string.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []

        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")

            elif i % 3 == 0:
                result.append("Fizz")

            elif i % 5 == 0:
                result.append("Buzz")

            else:
                result.append(str(i))

        return result
