class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1

        while l<=r:
            middle = l+(r-l)//2
            number = nums[middle]
            if target==number:
                return middle
            if number>target:
                r=middle-1
            else:
                l=middle+1

        return -1