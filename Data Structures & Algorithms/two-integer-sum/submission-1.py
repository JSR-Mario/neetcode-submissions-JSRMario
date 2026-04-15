class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complementos = {}

        for i,n in enumerate(nums):
            if target-n in complementos:
                return [complementos[target-n],i]
            complementos[n] = i