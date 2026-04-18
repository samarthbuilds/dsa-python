"""
Problem: Distribute Candies

Approach:
The sister can eat at most n/2 candies.
Use a set to count unique candy types and return the minimum
between the number of unique types and n/2.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(set(candyType)), len(candyType) // 2)
