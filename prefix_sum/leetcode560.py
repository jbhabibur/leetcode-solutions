"""
LeetCode Problem: 560. Subarray Sum Equals K
URL             : https://leetcode.com/problems/subarray-sum-equals-k/

Description:
    Given an integer array `nums` and an integer `k`, return the total number of
    subarrays whose sum equals to `k`.

Approach:
    1. Compute the prefix sum for each index in the array.
    2. Use a hash map to store the frequency of prefix sums seen so far.
    3. For each prefix sum `currSum`, check if there exists a prefix sum `currSum - k`.
       If it exists, it means there is a subarray ending at current index that sums to k.
    4. Also check if the current prefix sum equals k (subarray from index 0 to current).
    5. Update the hash map with the current prefix sum.

Time Complexity:
    O(n) — We iterate over the array once, doing constant time operations.

Space Complexity:
    O(n) — For storing prefix sum frequencies in a hash map.

Language: Python
"""

from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Step 1: Calculate prefix sum
        n = len(nums)
        ps = [0] * n
        ps[0] = nums[0]

        for i in range(1, len(nums)):
            ps[i] = ps[i - 1] + nums[i]

        # Step 2: Frequency map and count
        count = 0
        hash_map = defaultdict(int)

        for j in range(n):
            # Case 1: If prefix sum == k
            if ps[j] == k:
                count += 1

            # Case 2: Check if (prefixSum - k) exists
            val = ps[j] - k
            if val in hash_map:
                count += hash_map[val]

            # Update frequency of current prefix sum
            hash_map[ps[j]] += 1

        return count

# Example usage
nums = [1, 1, 1]
k = 2
sol = Solution()
print(sol.subarraySum(nums, k))