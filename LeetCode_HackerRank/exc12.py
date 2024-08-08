from typing import List

class Solution():
    def mergeTwoLists(self, arr_1: List[int], arr_2: List[int]) -> int:
        arr_final = []
        
        for i in arr_1:
            arr_final.append(i)
        for i in arr_2:
            arr_final.append(i)

        arr_final.sort()
        return arr_final

solution = Solution()
print(solution.mergeTwoLists([], [0]))

