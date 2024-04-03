from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        newDigits = int(''.join(str(digits[i]) for i in range(0, len(digits)))) + 1
        digits = [int(i) for i in str(newDigits)]

        return digits

obj = Solution()
print(obj.plusOne([1342]))
        