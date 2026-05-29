"""
Problem: Largest Number At Least Twice of Others

Approach:
Find the largest number and its index.
Then find the second largest number by iterating through the array.
If the largest number is at least twice the second largest,
return its index; otherwise return -1.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = max(nums)
        index = nums.index(largest)
        second = float('-inf')

        for num in nums:
            if num != largest:
                second = max(second, num)

        if largest >= 2 * second:
            return index

        return -1
