"""
LeetCode Problem: 1. Two Sum
URL             : https://leetcode.com/problems/two-sum/

Problem:
    Given an array of integers `nums` and an integer `target`,
    return indices of the two numbers such that they add up to `target`.

    You may assume that each input would have exactly one solution,
    and you may not use the same element twice.

    You can return the answer in any order.
"""

# ------------------------------ 1. Brute-Force ------------------------------ #
"""
Approach: Brute Force (Nested Loops)

Explanation:
    - Iterate through all pairs of indices (i, j) such that i < j
    - For each pair, check if nums[i] + nums[j] == target
    - If found, return [i, j]

    This checks every possible pair in the array.

Time Complexity : O(n^2) — two nested loops
Space Complexity: O(1)   — no extra space used
"""


from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

# Example usage
nums = [2,7,11,15]
target = 9
sol = Solution()
sol.twoSum(nums, target)