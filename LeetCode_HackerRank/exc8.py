from typing import List

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        numStr = int(''.join(str(num[i]) for i in range(0, len(num))))
        newSum = numStr + k

        num = [int(i) for i in str(newSum)]

        return num

obj = Solution()
print(obj.addToArrayForm([2,7,4], 181))