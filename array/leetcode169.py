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


# ------------------------------ 3. Optimized (Hash Map) ------------------------------ #
"""
Approach: Hash Map (Frequency Counting)

Explanation:
    - Use a hash map (dictionary) to count the frequency of each element in `nums`.
    - Iterate through the array once and update counts in the hash map.
    - After counting, iterate through the hash map to find the element
      whose frequency is greater than n // 2 and return it.

    This approach efficiently counts frequencies in a single pass and
    then finds the majority element in linear time.

Time Complexity : O(n) — single pass for counting + single pass for checking
Space Complexity: O(n) — hash map stores frequency of elements
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = {}

        # Performs O(n) times
        # Count the frequency of each number
        for num in nums:
            if num not in hash_map:
                hash_map[num] = 1
            else:
                hash_map[num] += 1

        # Performs O(n) times
        # Return the number whose frequency is greater than n//2
        for key, value in hash_map.items():
            if value > len(nums) // 2:
                return key


# ------------------------------ 4. Optimized (Boyer-Moore Voting) ------------------------------ #
"""
Approach: Boyer-Moore Voting Algorithm

Explanation:
    - Initialize two variables: `majority` (candidate element) and `voting` (counter).
    - Iterate through the array:
        - When `voting` is 0, pick the current element as the new candidate.
        - If the current element matches the candidate, increment `voting`.
        - Otherwise, decrement `voting`.
    - The candidate at the end is guaranteed to be the majority element.

    This approach uses O(1) space and O(n) time.

Time Complexity : O(n) — single pass through the array
Space Complexity: O(1) — constant space usage
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = 0 # Candidate
        voting = 0

        for num in nums:
            # If voting count drops to zero, choose a new candidate
            if voting == 0:
                majority = num

            # If current number matches candidate, increment voting count
            if num == majority:
                voting += 1
            else:
                # Otherwise, decrement voting count
                voting -= 1

        # At the end, 'majority' holds the majority element
        return majority