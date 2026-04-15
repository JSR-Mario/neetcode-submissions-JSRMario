class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        maximum = 0
        queue = deque()
        ROWS, COLS = len(grid),len(grid[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    curr_area = 1
                    queue.append((r,c))
                    grid[r][c]=2
                    while queue:
                        row, col = queue.popleft()
                        for dr,dc in directions:
                            new_row, new_col = row+dr,col+dc
                            if 0<=new_row<ROWS and 0<=new_col<COLS and grid[new_row][new_col]==1:
                                queue.append((new_row,new_col))
                                grid[new_row][new_col]=2
                                curr_area +=1
                    maximum = max(maximum,curr_area)
        return maximum