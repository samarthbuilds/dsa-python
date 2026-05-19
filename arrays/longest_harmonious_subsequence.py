"""
Problem: Longest Harmonious Subsequence

Approach:
Use a hashmap to count the frequency of each number.
For every number, check if num + 1 exists in the hashmap.
If it does, calculate the combined frequency and update
the maximum harmonious subsequence length.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        longest = 0

        for num in count:
            if num + 1 in count:
                longest = max(longest, count[num] + count[num + 1])

        return longest
