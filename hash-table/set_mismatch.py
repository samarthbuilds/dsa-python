"""
Problem: Set Mismatch

Approach:
Use a set to track seen numbers and find the duplicate.
Then iterate from 1 to n to find the missing number that is not in the set.
Return both duplicate and missing numbers.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        duplicate = -1

        for num in nums:
            if num in seen:
                duplicate = num
            else:
                seen.add(num)

        for i in range(1, len(nums) + 1):
            if i not in seen:
                return [duplicate, i]
