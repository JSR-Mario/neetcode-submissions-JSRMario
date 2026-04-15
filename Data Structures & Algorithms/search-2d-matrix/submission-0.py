class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for n in matrix:
            l,r=0,len(n)-1
            if target>=n[l] and target<=n[r]:
                while l<=r:
                    middle = l+(r-l)//2
                    number = n[middle]
                    if number==target:
                        return True
                    if number<target:
                        l=middle+1
                    else:
                        r=middle-1
        return False