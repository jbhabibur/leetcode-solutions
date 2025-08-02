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


# ------------------------------ 2. Optimized (Two Pointers) ------------------------------ #
"""
Approach: Two Pointers

Explanation:
    - Since the array is sorted, use two pointers: left at start, right at end.
    - While left < right:
        - Calculate current_sum = numbers[left] + numbers[right]
        - If current_sum == target: return [left + 1, right + 1]
        - If current_sum < target: move left pointer to the right
        - If current_sum > target: move right pointer to the left

    This approach leverages the sorted property for efficient search.

Time Complexity : O(n) — single pass through the array
Space Complexity: O(1) — no extra space used
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1

        while start < end:
            summation = numbers[start] + numbers[end]

            if summation == target:
                return [start + 1, end + 1]     # 1-indexed array
            elif summation < target:
                start += 1
            else:
                end -= 1