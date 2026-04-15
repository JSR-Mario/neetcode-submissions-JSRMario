class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l,r=0,n-1
        while l<r:
            mid = l+(r-l)//2
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid
        
        # ahora l==r y l es el starting original del arreglo
        if target==nums[l]:
            return l
        def bs(l,r):
            while l<=r:
                mid = l+(r-l)//2
                mid_num = nums[mid]
                if target==mid_num:
                    return mid
                if target>mid_num:
                    l=mid+1
                else:
                    r=mid-1
            return -1

        if target>nums[l] and target<=nums[-1]:
            return bs(l+1,n-1)
        
        return bs(0,l-1)