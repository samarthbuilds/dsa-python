"""
Problem: Third Maximum Number

Approach:
Maintain three variables to track the first, second, and third
largest unique numbers. Skip duplicates while iterating.
Update the values accordingly whenever a larger number is found.
If a third maximum does not exist, return the maximum number.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = float('-inf')

        for num in nums:
            if num in (first, second, third):
                continue

            if num > first:
                third = second
                second = first
                first = num

            elif num > second:
                third = second
                second = num

            elif num > third:
                third = num

        return third if third != float('-inf') else first
