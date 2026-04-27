"""
Problem: Self Dividing Numbers

Approach:
Check each number in the given range.
For every number, extract each digit and verify that:
1. The digit is not 0
2. The original number is divisible by that digit

If both conditions are satisfied for all digits,
add the number to the result list.

Time Complexity: O(n * d)
Space Complexity: O(1)
"""

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def isSelfDividing(num):
            temp = num

            while temp > 0:
                digit = temp % 10

                if digit == 0 or num % digit != 0:
                    return False

                temp //= 10

            return True

        result = []

        for num in range(left, right + 1):
            if isSelfDividing(num):
                result.append(num)

        return result
