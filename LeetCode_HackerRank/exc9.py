from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        position = []
        for i in range(len(nums)):
            if nums[i] == target:
                position.append(i)
        
        

        return position
    

obj = Solution()
print(obj.searchRange([1,2,3,4,4,5], 4))