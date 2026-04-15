class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # target-nums[i] = complement
        complements = {}
        for i,n in enumerate(nums):
            if target-nums[i] in complements:
                return [complements[target-nums[i]],i]
            complements[n]=i
        return [-1,-1]