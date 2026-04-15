class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        maximo = 0

        l,r = 0, n-1

        while l<r:
            if heights[l]<heights[r]:
                if (r-l)*heights[l]>maximo:
                    maximo = (r-l)*heights[l]
                l+=1
            else:
                if (r-l)*heights[r]>maximo:
                    maximo = (r-l)*heights[r]
                r-=1
        
        return maximo