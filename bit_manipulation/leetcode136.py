"""
LeetCode Problem: 136. Single Number
URL             : https://leetcode.com/problems/single-number/

Problem:
    Given a non-empty array of integers `nums`, every element appears twice except for one.
    Find that single one.

    You must implement a solution with a linear runtime complexity and use only constant extra space.

Constraints:
    - 1 <= nums.length <= 3 * 10^4
    - -3 * 10^4 <= nums[i] <= 3 * 10^4
    - Each element in the array appears twice except for one element which appears only once.
"""


# ------------------------------ 1. Brute Force Approach ------------------------------ #
"""
Approach: Brute Force using Nested Loops

Explanation:
    - For each element in the list:
        - Count how many times it appears by looping over the entire list again.
    - If it appears only once, return it.

    This is a naive solution and doesn't meet the optimal constraints,
    but it's useful for understanding the logic.

Time Complexity : O(n^2) — for each element, we scan the array again to count occurrences
Space Complexity: O(1)   — no additional data structures used
"""

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            count = 0
            for j in range(n):
                if nums[i] == nums[j]:
                    count += 1

            if count == 1:
                return nums[i]

# Example usage
nums = [1, 2, 1, 2, 3]
sol = Solution()
print(sol.singleNumber(nums))


#------------------------------ 2. Hash Map Approach ------------------------------ ##
"""
Approach: Using Hash Map (Dictionary)

Explanation:
    - Use a hash map to store the count of each number.
    - Traverse the list once to fill the hash map with frequencies.
    - Traverse the hash map to find the number that appears exactly once.

    This approach satisfies linear time complexity but uses extra space,
    so it doesn't meet the "constant space" constraint.

Time Complexity : O(n) — one pass to count, one pass to find the single number
Space Complexity: O(n) — additional space used for storing frequencies
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import defaultdict
        hash_map = defaultdict(int)

        # Count occurrences takes 0(n) times
        for num in nums:
            hash_map[num] += 1

        # To find the number that appears once takes 0(n)
        for key, value in hash_map.items():
            if value == 1:
                return key


# ------------------------------ 3. Bitwise XOR Approach ------------------------------ #
"""
Approach: Bitwise XOR

Explanation:
    - XOR of a number with itself is 0 (a ^ a = 0)
    - XOR of a number with 0 is the number itself (a ^ 0 = a)
    - So, all numbers that appear twice cancel each other out.
    - The remaining number is the one that appears only once.

Time Complexity : O(n) — only one pass through the list
Space Complexity: O(1) — constant extra space used
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0

        for num in nums:
            xor ^= num

        return xor