class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        maximo = 0

        while l<r:
            maximo = max(min(heights[l],heights[r])*(r-l), maximo)

            if heights[l]<=heights[r]:
                l+=1
            else:
                r-=1
        
        return maximo