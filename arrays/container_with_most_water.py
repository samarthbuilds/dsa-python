"""
Problem: Container With Most Water

Approach:
Use two pointers at the beginning and end of the array.
Calculate the area formed by the two lines and update the maximum area.
Move the pointer pointing to the shorter line inward, since moving the
taller line cannot increase the area while the width decreases.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        ans = 0

        while left < right:
            width = right - left
            h = min(height[left], height[right])

            ans = max(ans, width * h)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return ans
