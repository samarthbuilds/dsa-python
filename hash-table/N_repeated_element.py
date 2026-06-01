"""
Problem: N-Repeated Element in Size 2N Array

Approach:
Use a set to keep track of elements that have already been seen.
While iterating through the array, if an element is already present
in the set, it is the repeated element and can be returned immediately.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen = set()

        for num in nums:
            if num in seen:
                return num

            seen.add(num)
