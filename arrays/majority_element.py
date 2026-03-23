"""
Problem: Majority Element

Approach:
Use Boyer-Moore Voting Algorithm. Maintain a candidate and a count.
If count becomes zero, choose the current element as the new candidate.
Increase count if the element matches the candidate, otherwise decrease it.
At the end, the candidate will be the majority element.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate
