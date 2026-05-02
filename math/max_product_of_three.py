"""
Problem: Maximum Product of Three Numbers

Approach:
Sort the array. The maximum product can be either:
1. Product of the three largest numbers
2. Product of the two smallest (negative) numbers and the largest number
Return the maximum of both cases.

Time Complexity: O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()

        return max(
            nums[-1] * nums[-2] * nums[-3],
            nums[0] * nums[1] * nums[-1]
        )
