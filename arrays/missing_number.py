"""
Problem: Missing Number

Approach:
Use the formula for the sum of first n natural numbers.
Calculate the expected sum using n*(n+1)//2 and subtract
the actual sum of the array to get the missing number.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected = n * (n + 1) // 2
        actual = sum(nums)

        return expected - actual
