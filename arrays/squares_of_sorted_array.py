"""
Problem: Squares of a Sorted Array

Approach:
Use two pointers at the beginning and end of the array.
Compare absolute values of both ends and place the larger square
at the current position from the end of the result array.
Move the corresponding pointer and continue until all elements are processed.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n

        left = 0
        right = n - 1
        pos = n - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[pos] = nums[left] * nums[left]
                left += 1
            else:
                result[pos] = nums[right] * nums[right]
                right -= 1

            pos -= 1

        return result
