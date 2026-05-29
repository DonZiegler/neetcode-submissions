class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols=len(grid),len(grid[0])

        islands=0

        def dfs(grid,row,col):
            if min(row,col)<0 or row>=rows or col>=cols or grid[row][col]=="0":
                return

            grid[row][col]="0"
            dfs(grid,row,col-1)
            dfs(grid,row,col+1)
            dfs(grid,row+1,col)
            dfs(grid,row-1,col)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1":
                    islands+=1
                    dfs(grid,r,c)



        return islands
