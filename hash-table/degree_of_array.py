"""
Problem: Degree of an Array

Approach:
Use hashmaps to store:
1. Frequency count of each number
2. First occurrence index of each number

Track the degree of the array while iterating.
Whenever a number reaches the current degree,
update the minimum subarray length.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = {}
        first = {}
        degree = 0
        min_len = len(nums)

        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i

            count[num] = count.get(num, 0) + 1

            if count[num] > degree:
                degree = count[num]
                min_len = i - first[num] + 1

            elif count[num] == degree:
                min_len = min(min_len, i - first[num] + 1)

        return min_len
