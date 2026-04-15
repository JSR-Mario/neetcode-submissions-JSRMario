class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        queue = deque()

        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]=='1':
                    islands+=1
                    queue.append((r,c))
                    grid[r][c]=2
                    while queue:
                        row,col = queue.popleft()
                        for y,x in directions:
                            nr,nc = row+y, col+x
                            if 0<=nr<ROWS and 0<=nc<COLS and grid[nr][nc]=='1':
                                queue.append((nr,nc))
                                grid[nr][nc]=2
        
        return islands