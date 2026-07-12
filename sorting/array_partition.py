"""
Problem: Array Partition

Approach:
Sort the array so that adjacent elements form optimal pairs.
The smaller element in each pair will be at every even index.
Sum all elements at even indices to maximize the total.

Time Complexity: O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0

        for i in range(0, len(nums), 2):
            ans += nums[i]

        return ans
