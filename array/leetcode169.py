"""
LeetCode Problem: 169. Majority Element
URL             : https://leetcode.com/problems/majority-element/

Problem:
    Given an array `nums` of size n, return the majority element.
    The majority element is the element that appears more than [n / 2] times.

    You may assume that the majority element always exists in the array.
"""


# ------------------------------ 1. Brute-Force ------------------------------ #
"""
Approach: Brute Force (Nested Loops)

Explanation:
    - Iterate through each element `nums[i]` in the array.
    - For each element, count how many times it appears in the entire array.
    - If count > n // 2, return that element as the majority.

    This approach directly checks frequency of every unique element.

Time Complexity : O(n^2) — nested loop to count frequency for each element
Space Complexity: O(1)   — no extra space used
"""

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            count = 0

            for j in range(n):
                if nums[j] == nums[i]:
                    count += 1

            if count > (n // 2):
                return nums[i]

# Example usage
nums = [3,2,3]
sol = Solution()
sol.majorityElement(nums)


# ------------------------------ 2. Optimized (Sorting) ------------------------------ #
"""
Approach: Sorting

Explanation:
    - First, sort the array `nums` in non-decreasing order.
    - Since the majority element appears more than n // 2 times,
      it will always occupy the middle index after sorting.
    - Simply return the element at index n // 2.

    Sorting brings the majority element into the center of the array.

Time Complexity : O(n log n) — due to sorting
Space Complexity: O(1)       — in-place sort (ignoring sort space)
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Sorting performs O(n log n) times
        nums.sort()

        # The majority element will always occupy the middle index after sorting
        middle_index = len(nums) // 2

        return nums[middle_index]