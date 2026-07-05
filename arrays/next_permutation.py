"""
Problem: Next Permutation

Approach:
Traverse the array from the end to find the first element that is
smaller than its next element (pivot). Then find the smallest element
greater than the pivot from the right side and swap them.
Finally, reverse the suffix after the pivot to obtain the next
lexicographically greater permutation.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2

        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            j = n - 1

            while nums[j] <= nums[i]:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]

        left = i + 1
        right = n - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
