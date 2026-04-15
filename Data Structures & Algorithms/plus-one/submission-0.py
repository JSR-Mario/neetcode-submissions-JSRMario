class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        number = 0

        for n in digits:
            number = number*10+n
        
        number += 1

        result = []
        while number>0:
            result.append(number%10)
            number//=10

        return result[::-1]