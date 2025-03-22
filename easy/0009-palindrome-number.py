"""
LeetCode Problem: 0009 - Palindrome Number

Difficulty: Easy
Tags: math

Problem Description:
    Given an integer x, return true if x is a palindrome, and false otherwise.

Constraints:
    • -231 <= x <= 231 - 1
"""

class Solution:
    def solve(self, x: int) -> bool:
        """
        Main solution method.

        Args:
            x (int): An integer.

        Returns:
            bool: True if x is a palindrome, and false otherwise.
        """
        # Negative numbers (x < 0) are not palindromes. Multiples of 10 (except 0) are also not palindromes (e.g., 10, 100).
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # Compares x == reversed_half for even-length or x == reversed_half // 10 (middle digit ignored) for odd-length: 
        return x == reversed_half or x == reversed_half // 10


# Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Example tests (modify as needed)
    print(solution.solve(121))  # Expected: True
    print(solution.solve(-121))  # Expected: False
    print(solution.solve(10))  # Expected: False
