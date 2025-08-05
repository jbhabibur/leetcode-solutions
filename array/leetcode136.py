from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            count = 0
            for j in range(n):
                if nums[j] == nums[i]:
                    count += 1

            if count == 1:
                return i


# Example usage
nums = [2,2,1]
sol = Solution()
print(sol.singleNumber(nums))