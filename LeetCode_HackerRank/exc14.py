from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(0, len(nums)):
            if target == nums[i]:
                return i
            if nums[i]:
                return i+1
            return i-1
            
a = Solution()
print(a.searchInsert([1,3,5,6], 7))