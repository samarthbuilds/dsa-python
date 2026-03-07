"""
Problem: Two Sum

Approach:
Use a hashmap to store numbers we have seen.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]

            seen[num] = i
