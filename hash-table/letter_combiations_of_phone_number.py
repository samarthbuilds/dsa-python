"""
Problem: Letter Combinations of a Phone Number

Approach:
Use backtracking to generate all possible letter combinations.
Maintain a mapping of digits to their corresponding letters.
At each digit, recursively choose one letter and move to the next digit.
When all digits have been processed, add the current combination to the result.

Time Complexity: O(4^n * n)
Space Complexity: O(n)
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []

        def backtrack(index, path):
            if index == len(digits):
                result.append(path)
                return

            letters = phone[digits[index]]

            for ch in letters:
                backtrack(index + 1, path + ch)

        backtrack(0, "")
        return result
