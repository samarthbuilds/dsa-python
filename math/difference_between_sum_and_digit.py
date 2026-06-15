"""
Problem: Difference Between Element Sum and Digit Sum of an Array

Approach:
Calculate the sum of all elements in the array.
Then extract and sum the digits of every number.
Return the absolute difference between the element sum
and the digit sum.

Time Complexity: O(n * d)
Space Complexity: O(1)
"""

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = sum(nums)
        digit_sum = 0

        for num in nums:
            while num > 0:
                digit_sum += num % 10
                num //= 10

        return abs(element_sum - digit_sum)
