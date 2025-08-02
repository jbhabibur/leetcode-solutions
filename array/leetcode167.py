"""
LeetCode Problem: 167. Two Sum II - Input Array Is Sorted
URL             : https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Problem:
    Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order,
    find two numbers such that they add up to a specific `target` number.

    Return the indices of the two numbers (1-indexed) such that they add up to `target`,
    where index1 < index2.

    You may assume that each input would have exactly one solution,
    and you may not use the same element twice.

    You must use only constant extra space.
"""

# ------------------------------ 1. Brute-Force ------------------------------ #
"""
Approach: Brute Force (Nested Loops)

Explanation:
    - Iterate through all pairs of indices (i, j) such that i < j
    - For each pair, check if numbers[i] + numbers[j] == target
    - If found, return [i + 1, j + 1] (since array is 1-indexed)

    This approach checks every possible pair in the array.

Time Complexity : O(n^2) — two nested loops
Space Complexity: O(1)   — no extra space used
"""

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        for i in range(n):
            for j in range(i + 1, n):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]       # 1-indexed array

# Example usage
nums = [2,7,11,15]
target = 9
sol = Solution()
sol.twoSum(nums, target)




