class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_of_islands = 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def mark_dfs(row, col):
            grid[row][col]=2
            for change_row, change_col in directions:
                new_row,new_col = row+change_row,col+change_col
                if new_row>=0 and new_row<ROWS and new_col>=0 and new_col<COLS and grid[new_row][new_col] == '1':
                    mark_dfs(new_row, new_col)


        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]=='1':
                    mark_dfs(i,j)
                    num_of_islands+=1

        return num_of_islands