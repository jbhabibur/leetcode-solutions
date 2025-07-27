"""
LeetCode Problem: Subarray Sums Divisible by K
URL             : https://leetcode.com/problems/subarray-sums-divisible-by-k/

Description:
    Given an integer array `nums` and an integer `k`,
    return the number of non-empty subarrays whose sum is divisible by `k`.

Approach - 1 (Brute-force):
    1. Use a brute-force triple nested loop to consider all possible subarrays.
    2. Calculate the sum of each subarray explicitly.
    3. Check if the sum is divisible by `k` and increment count if so.

Time Complexity:
    O(n^3) — Due to three nested loops iterating over all subarrays and their sums.

Space Complexity:
    O(1) — Only a constant amount of extra space is used.

Language: Python
"""

from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0

        for i in range(n):
            for j in range(i, n):
                current_sum = 0
                for m in range(i, j + 1):
                    current_sum += nums[m]

                if current_sum % k == 0:
                    count += 1

        return count

# Example usage
nums = [4, 5, 0, -2, -3, 1]
k = 5
sol = Solution()
print(sol.subarraysDivByK(nums, k))  # Output: 7

"""
Approach - 2 (Prefix Sum - In-place):
    1. Modify the input array in-place to store prefix sums.
    2. Iterate over all possible subarrays using indices i and j.
    3. Use the prefix sums to calculate each subarray's sum efficiently:
        - If i == 0, subarray sum is nums[j]
        - Else, subarray sum is nums[j] - nums[i - 1]
    4. Check if the subarray sum is divisible by k and increment count if true.

Time Complexity:
    O(n^2) — Two nested loops to evaluate all subarrays.

Space Complexity:
    O(1) — Constant extra space; prefix sums computed in-place.
"""

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0

        # Compute cumulative (prefix) sum
        for i in range(1, n):
            nums[i] += nums[i - 1]

        # Check all subarrays
        for i in range(n):
            for j in range(i, n):
                # Compute subarray sum from i to j
                sub_sum = nums[j] if i == 0 else nums[j] - nums[i - 1]

                # Check if divisible by k
                if sub_sum % k == 0:
                    count += 1

        return count