class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mult = nums[0]
        n = len(nums)
        result = [1]*n

        for i in range(1,n):
            result[i] = mult
            mult*=nums[i]
        
        mult = nums[-1]
        for i in range(n-2,-1,-1):
            result[i]*=mult
            mult*=nums[i]

        return result