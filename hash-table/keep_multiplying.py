"""
Problem: Keep Multiplying Found Values by Two

Approach:
Store all numbers in a set for O(1) lookups.
While the current value exists in the set,
multiply it by 2. Return the final value once
it is no longer present in the set.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums_set = set(nums)

        while original in nums_set:
            original *= 2

        return original
