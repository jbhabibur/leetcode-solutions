from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        for i in range(n):
            if i == 0 and nums[i] != nums[i + 1]:
                return nums[i]
            elif i == n - 1 and

# Example usage
nums = [1, 1, 1, 2, 2, 2, 3, 4, 4, 4]
sol = Solution()
print(sol.singleNumber(nums))