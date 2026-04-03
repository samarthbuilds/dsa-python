"""
Problem: Remove Element

Approach:
Use a pointer `k` to track the position for the next valid element.
Iterate through the array and whenever an element is not equal to `val`,
place it at index `k` and increment `k`. This overwrites unwanted elements.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k
