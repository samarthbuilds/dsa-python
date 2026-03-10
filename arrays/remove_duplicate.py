"""
Problem: Remove Duplicates from Sorted Array

Approach:
Since the array is sorted, duplicates will appear next to each other.
Use a pointer `k` to track the position of the next unique element.
Iterate through the array and whenever a new unique number is found,
place it at index `k` and increment `k`.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1

        return k
