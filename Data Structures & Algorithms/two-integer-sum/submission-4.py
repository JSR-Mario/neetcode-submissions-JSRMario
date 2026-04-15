class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        for i,n in enumerate(nums):
            if target-n in complements:
                return [complements[target-n],i]
            complements[n] = i
        
        return [-1,-1]