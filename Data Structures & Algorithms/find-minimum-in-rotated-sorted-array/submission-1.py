class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            medium = l+(r-l)//2
            if medium>0 and nums[medium-1]>nums[medium]:
                return nums[medium]
            if nums[medium]>nums[r]:
                l=medium+1
            else:
                r=medium-1
        return nums[l]