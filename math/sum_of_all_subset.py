"""
Problem: Sum of All Subset XOR Totals

Approach:
Use backtracking (DFS) to generate all possible subsets.
For each element, make two recursive calls:
1. Include the element in the current subset XOR
2. Exclude the element

When all elements have been processed, add the current XOR
value to the final answer.

Time Complexity: O(2^n)
Space Complexity: O(n)
"""

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0

        def dfs(index, curr_xor):
            nonlocal ans

            if index == len(nums):
                ans += curr_xor
                return

            dfs(index + 1, curr_xor ^ nums[index])
            dfs(index + 1, curr_xor)

        dfs(0, 0)

        return ans
