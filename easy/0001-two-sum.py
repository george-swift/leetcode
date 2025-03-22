"""
LeetCode Problem: 0001 - Two Sum

Difficulty: Easy
Tags: array, hashtable

Problem Description:
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.

Constraints:
    • 2 <= nums.length <= 10^4
    • -10^9 <= nums[i] <= 10^9
    • -10^9 <= target <= 10^9
    • Only one valid answer exists.
"""

from typing import List

class Solution:
    def solve(self, nums: List[int], target: int) -> List[int]:
        """
        Main solution method.

        Args:
            nums (List[int]): The input array of integers.
            target (int): The target sum.

        Returns:
            List[int]: Indices of the two numbers adding up to the target.
        """
        seen = {}
        for index, number in enumerate(nums):
            complement = target - number
            if complement in seen:
                return [seen[complement], index]
            seen[number] = index
        return []
        


# Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Example tests (modify as needed)
    print(solution.solve([2, 7, 11, 15], 9))  # Expected: [0, 1]
    print(solution.solve([3, 2, 4], 6))       # Expected: [1, 2]
    print(solution.solve([3, 3], 6))          # Expected: [0, 1]
