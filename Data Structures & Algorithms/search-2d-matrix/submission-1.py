class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # neetcode solution 
        ROWS, COLS = len(matrix), len(matrix[0])

        l,r = 0, ROWS*COLS-1
        while l<=r:
            m = l+(r-l)//2
            row,col = m//COLS, m%COLS
            number = matrix[row][col]
            if target == number:
                return True
            if target>number:
                l=m+1
            else:
                r=m-1
        return False