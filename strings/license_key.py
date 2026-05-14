"""
Problem: License Key Formatting

Approach:
Remove all dashes and convert the string to uppercase.
Process the string from the end in groups of size k
and store each group in a list. Finally reverse the list
and join the groups using dashes.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        cleaned = s.replace("-", "").upper()
        result = []

        while len(cleaned) > k:
            result.append(cleaned[-k:])
            cleaned = cleaned[:-k]

        result.append(cleaned)

        return "-".join(result[::-1])
