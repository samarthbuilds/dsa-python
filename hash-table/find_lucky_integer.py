"""
Problem: Find Lucky Integer in an Array

Approach:
Use a hashmap to count the frequency of each number.
Then iterate through the frequency map and check whether
a number is equal to its frequency. Keep track of the
largest such number and return it.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = {}

        for num in arr:
            count[num] = count.get(num, 0) + 1

        ans = -1

        for num, freq in count.items():
            if num == freq:
                ans = max(ans, num)

        return ans
