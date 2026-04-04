"""
Problem: Move Zeroes

Approach:
Use a pointer `j` to track the position of the next non-zero element.
Iterate through the array and whenever a non-zero element is found,
swap it with the element at index `j` and increment `j`.
This moves all non-zero elements forward and zeroes to the end.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
