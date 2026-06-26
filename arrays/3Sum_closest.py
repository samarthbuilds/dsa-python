"""
Problem: 3Sum Closest

Approach:
Sort the array and fix one element at a time.
Use two pointers to find the pair whose sum, along with the fixed element,
is closest to the target. Update the closest sum whenever a better
candidate is found. If an exact match is found, return it immediately.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if abs(target - total) < abs(target - closest):
                    closest = total

                if total < target:
                    left += 1

                elif total > target:
                    right -= 1

                else:
                    return total

        return closest
