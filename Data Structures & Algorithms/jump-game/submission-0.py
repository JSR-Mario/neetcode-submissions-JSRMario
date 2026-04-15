class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        if length==1:
            return True
        
        power = nums[0]
        if power==0:
            return False
        if power>=length:
            return True
        
        for i,n in enumerate(nums):
            power-=1
            if n>power:
                power = n
            if power==0 and i<length-1:
                return False
        return True