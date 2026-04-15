class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l,r = 0, len(heights)-1
        while l<r:
            lh,rh = heights[l],heights[r]
            curr_area = min(lh,rh)*(r-l)
            max_area  = max(max_area,curr_area)

            if lh<rh:
                l+=1
            else:
                r-=1
            
        return max_area