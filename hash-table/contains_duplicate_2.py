"""
Problem: Contains Duplicate II

Approach:
Use a hashmap to store the last seen index of each number.
While iterating, if the number is already in the hashmap,
check the difference between current index and previous index.
If it is less than or equal to k, return True.
Otherwise, update the index.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = {}

        for i, num in enumerate(nums):
            if num in index_map:
                if i - index_map[num] <= k:
                    return True

            index_map[num] = i

        return False
