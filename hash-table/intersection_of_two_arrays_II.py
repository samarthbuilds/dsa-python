"""
Problem: Intersection of Two Arrays II

Approach:
Use a hashmap to store the frequency of elements in nums1.
Iterate through nums2 and if an element exists in the hashmap
with a positive count, add it to the result and decrease its count.

Time Complexity: O(n + m)
Space Complexity: O(n)
"""

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = {}

        for num in nums1:
            count[num] = count.get(num, 0) + 1

        result = []

        for num in nums2:
            if num in count and count[num] > 0:
                result.append(num)
                count[num] -= 1

        return result
