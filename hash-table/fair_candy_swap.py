"""
Problem: Fair Candy Swap

Approach:
Calculate the total candies Alice and Bob have.
The required difference determines the candy size Bob should give
for each candy Alice gives. Store Bob's candy sizes in a set for
fast lookup and return the first valid swap.

Time Complexity: O(n + m)
Space Complexity: O(m)
"""

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)
        diff = (sumB - sumA) // 2

        bob_set = set(bobSizes)

        for x in aliceSizes:
            if x + diff in bob_set:
                return [x, x + diff]
