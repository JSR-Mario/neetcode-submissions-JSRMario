class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        DIRECTIONS  = ((-1,0),(1,0),(0,-1),(0,1))
        ROWS,COLS   = len(grid),len(grid[0])

        queue       = deque()
        fresh_count = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==2:
                    queue.append((r,c))
                elif grid[r][c]==1:
                    fresh_count+=1

        time = 0
        if fresh_count == 0:
                return time
        while queue:
            if fresh_count == 0:
                return time
            for _ in range(len(queue)):
                curr_r,curr_c = queue.popleft()
                for cr, cc in DIRECTIONS:
                    nr, nc = curr_r + cr, curr_c+cc
                    if 0<=nr<ROWS and 0<=nc<COLS and grid[nr][nc]==1:
                        fresh_count-=1
                        grid[nr][nc]=2
                        queue.append((nr,nc))
            time+=1

        return -1