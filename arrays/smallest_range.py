"""
Problem: Smallest Range I

Approach:
The maximum value can be decreased by k and the minimum value
can be increased by k. This reduces the range by 2 * k.
If the reduced range becomes negative, return 0.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        return max(0, max(nums) - min(nums) - 2 * k)
