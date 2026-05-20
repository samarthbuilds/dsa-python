"""
Problem: Sort Array By Parity

Approach:
Use two pointers, one from the beginning and one from the end.
If the left element is odd and the right element is even, swap them.
Move the left pointer forward when it points to an even number,
and move the right pointer backward when it points to an odd number.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] % 2 > nums[right] % 2:
                nums[left], nums[right] = nums[right], nums[left]

            if nums[left] % 2 == 0:
                left += 1

            if nums[right] % 2 == 1:
                right -= 1

        return nums
