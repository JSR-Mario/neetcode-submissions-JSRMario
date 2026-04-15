class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid),len(grid[0])
        queue = deque()
        fresh = 0

        for i in range(ROWS):
            for j in range (COLS):
                if grid[i][j]==2:	
                    queue.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        if fresh==0:
            return 0
	
        direction_array = [(-1,0),(1,0),(0,-1),(0,1)]
        minute = 0
        while queue and fresh:
            minute+=1
            for _ in range(len(queue)):
                r,c = queue.popleft()
                for rc,cc in direction_array:
                    nr, nc = r+rc, c+cc
                    if 0<=nr<ROWS and 0<=nc<COLS and grid[nr][nc]==1:
                        grid[nr][nc] = grid[r][c]+1
                        queue.append((nr,nc))
                        fresh-=1

        return minute if fresh==0 else -1