class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        l,r = 0,n-1
        maxLeft,maxRight,minimos= [0]*n,[0]*n,[0]*n

        maximo = 0
        for i in range(1,n):
            maximo=maxLeft[i]=max(maximo,height[i-1])
        
        maximo = 0
        for i in range(n-2,-1,-1):
            maximo=maxRight[i]=max(maximo,height[i+1])

        for i in range(n):
            minimos[i]=min(maxRight[i],maxLeft[i])
        
        answer=0
        for i in range(n):
            agua = minimos[i]-height[i]
            answer += agua if agua>0 else 0

        return answer