class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS=len(grid), len(grid[0])
        if min(ROWS,COLS)==0:
            return 0

        max_size=0

        def search_recur(r, c):
            if r>=ROWS or c>=COLS or min(r,c)<0 or grid[r][c]==0:
                return 0

            # Must be on a island
            grid[r][c]=0

            return 1+search_recur(r+1,c)+search_recur(r-1,c)+search_recur(r,c+1)+search_recur(r,c-1)


        for i in range(ROWS):
            for j in range(COLS):
                val=search_recur(i,j)
                if val > max_size:
                    max_size=val


        return max_size