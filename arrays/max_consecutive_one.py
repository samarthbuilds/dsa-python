"""
Problem: Max Consecutive Ones

Approach:
Traverse the array and maintain a count of consecutive 1s.
If the current element is 1, increment the count and update
the maximum count seen so far. If the element is 0, reset the count.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        ans = 0

        for num in nums:
            if num == 1:
                count += 1
                ans = max(ans, count)
            else:
                count = 0

        return ans
